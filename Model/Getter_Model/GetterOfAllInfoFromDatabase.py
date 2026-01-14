import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import select
from sqlalchemy.orm import Session
from Model.Pool import Mysql_Pool
from itertools import zip_longest
from Model.SQLAlchemy.schema import  Circuit_Model, Contact, Contact_Model_without_Pydantic, Itinerary_Model,Adrenaline_Model,Equipement_Model,Included_task_in_Price_Model, Modelised_Value


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
    #data dejà modeliser depuis l'API distant
    async def __Fetch_Tour_Data_From_Database(self):
        result:Modelised_Value = requests.get("http://localhost:5000").json()
        await asyncio.to_thread(self.__Convert_Dict_Into_Class,result)
    async def __Convert_Dict_Into_Class(self,element:Modelised_Value):
        self.circuit.clear()
        self.adrenaline.clear()
        self.itineraire.clear()
        self.equipement_needed.clear()
        self.included.clear()

        for circuit,adrenaline,equipement,itinerary,included in zip_longest(element.circuit,element.adrenaline,element.equipement,element.itineraire,element.included,fillvalue=None):
            await self.circuit.append(Circuit_Model(id=circuit.id,title=circuit.title,subtitle=circuit.subtitle,description=circuit.description,duration=circuit.duration,difficulty=circuit.difficulty,price=circuit.price,image=circuit.image))
            await self.adrenaline.append(Adrenaline_Model(id=adrenaline.id,content=adrenaline.content,circuit_id=adrenaline.circuit_id))
            await self.itineraire.append(Itinerary_Model(id=itinerary.id,place=itinerary.place,order_id=itinerary.order_id,circuit_id=itinerary.circuit_id))
            await self.equipement_needed.append(Equipement_Model(id=equipement.id,equipment=equipement.equipment,circuit_id=equipement.circuit_id))
            await self.included.append(Included_task_in_Price_Model(id=included.id,content=included.content,circuit_id=included.circuit_id))