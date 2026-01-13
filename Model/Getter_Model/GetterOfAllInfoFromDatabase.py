import asyncio
from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import select
from sqlalchemy.orm import Session
from Model.Pool import Mysql_Pool
from Model.SQLAlchemy.schema import Adrenaline, Circuit, Circuit_Model, Contact, Contact_Model_without_Pydantic, Equipement, Included_task_in_Price, Itinerary,Itinerary_Model,Adrenaline_Model,Equipement_Model,Included_task_in_Price_Model


class Instance_of_All_Data(Mysql_Pool):
    circuit:list[Circuit_Model] = []
    adrenaline:list[Adrenaline_Model]  = []
    itineraire:list[Itinerary_Model] = []
    equipement_needed:list[Equipement_Model] = []
    included:list[Included_task_in_Price_Model] = []
    contact:list[Contact_Model_without_Pydantic] = []
    def __init__(self):
        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.submit(asyncio.run,self.Worker())
    
    async def Worker(self):
        while True:
            await asyncio.to_thread(self.__Fetch_Tour_Data_From_Database)
            await asyncio.to_thread(self.__Fetch_Contact_Data_From_Database)
            await asyncio.sleep(3600/2)
    
    async def __Append_To_Contact_List(self,contact:Contact):
        self.contact.clear()
        await self.contact.append(Contact_Model_without_Pydantic(id=contact.id,name=contact.name,subject=contact.subject,body=contact.body,mail=contact.mail,number=contact.number,begining=contact.begining,number_of_person=contact.number_of_person,circuit_id=contact.circuit_id,total_price=contact.total_price,Completed=contact.Completed))

    async def __Fetch_Contact_Data_From_Database(self):
        with Session(self._engine) as session:
            get_data_in_join = select(Contact)
            for element in session.scalars(get_data_in_join):
                await self.__Append_To_Contact_List(element)
            await asyncio.sleep(36)
    async def __Fetch_Tour_Data_From_Database(self):
        with Session(self._engine) as session:
            get_data_in_join = select(Circuit,Adrenaline,Itinerary,Equipement,Included_task_in_Price).outerjoin(Circuit.adrenaline).outerjoin(Circuit.itinerary).outerjoin(Circuit.equipment_needed).outerjoin(Circuit.included_in_price)
            data_brute = await session.scalars(get_data_in_join).all()
            for circuit,adrenaline,itinerary,equipement,included in data_brute:
                await asyncio.to_thread(self.__Convert_Dict_Into_Class,circuit,adrenaline,itinerary,equipement,included)
            await asyncio.sleep(36)

    async def __Convert_Dict_Into_Class(self,circuit,adrenaline,itinerary,equipement,included):
        self.circuit.clear()
        self.adrenaline.clear()
        self.itineraire.clear()
        self.equipement_needed.clear()
        self.included.clear()
        circuit_dict = circuit.__dict__
        await self.circuit.append(Circuit_Model(id=circuit_dict["id"],title=circuit_dict["title"],subtitle=circuit_dict["subtitle"],description=circuit_dict["description"],duration=circuit_dict["duration"],difficulty=circuit_dict["difficulty"],price=circuit_dict["price"],image=circuit_dict["image"]))
        adrenaline_dict = adrenaline.__dict__
        await self.adrenaline.append(Adrenaline_Model(id=adrenaline_dict["id"],content=adrenaline_dict["content"],circuit_id=adrenaline_dict["circuit_id"]))
        itinerary_dict = itinerary.__dict__
        await self.itineraire.append(Itinerary_Model(id=itinerary_dict["id"],place=itinerary_dict["place"],order_id=itinerary_dict["order_id"],circuit_id=itinerary_dict["circuit_id"]))
        equipement_dict = equipement.__dict__
        await self.equipement_needed.append(Equipement_Model(id=equipement_dict["id"],equipment=equipement_dict["equipment"],circuit_id=equipement_dict["circuit_id"]))
        included_dict = included.__dict__
        await self.included.append(Included_task_in_Price_Model(id=included_dict["id"],content=included_dict["content"],circuit_id=included_dict["circuit_id"]))