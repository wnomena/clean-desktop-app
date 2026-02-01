import asyncio
import aioschedule
import requests
from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import Session
from Model.Pool import Mysql_Pool
from itertools import zip_longest
from Model.SQLAlchemy.schema import  Circuit_Model, Contact, Contact_Model_without_Pydantic, Data, Itinerary_Model,Adrenaline_Model,Equipement_Model,Included_task_in_Price_Model, ResponseFetch


class Instance_of_All_Data(Mysql_Pool):
    circuit:list[Circuit_Model] = []
    adrenaline:list[Adrenaline_Model]  = []
    itineraire:list[Itinerary_Model] = []
    equipement_needed:list[Equipement_Model] = []
    included:list[Included_task_in_Price_Model] = []
    contact:list[Contact_Model_without_Pydantic] = []
    def __init__(self):
        super().__init__()
        if self._engine:
            self.async_session = async_sessionmaker(self._engine,expire_on_commit=False)
            with ThreadPoolExecutor(max_workers=2) as executor:
                asyncio.run(self.__Fetch_Tour_Data_From_Database())
                asyncio.run(self.__Fetch_Contact_Data_From_Database())
                executor.submit(asyncio.run,self.Worker())
    
    async def Worker(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop=loop)
        aioschedule.every(1).hour.do(self.__Fetch_Tour_Data_From_Database)
        aioschedule.every(1).hour.do(self.__Fetch_Contact_Data_From_Database)
        while True:
            loop.run_until_complete(lambda:aioschedule.run_pending())
            asyncio.sleep(0)        
    
    async def __Append_To_Contact_List(self,contact:Contact):
        self.contact.clear()
        self.contact.append(Contact_Model_without_Pydantic(id=contact.id,name=contact.name,subject=contact.subject,body=contact.body,mail=contact.mail,number=contact.number,begining=contact.begining,number_of_person=contact.number_of_person,circuit_id=contact.circuit_id,total_price=contact.total_price,Completed=contact.Completed))

    async def __Fetch_Contact_Data_From_Database(self):
        async with self.async_session() as session:
            get_data_in_join = select(Contact)
            brut_data = await session.scalars(get_data_in_join)
            for element in brut_data:
                print(element.name)
                await self.__Append_To_Contact_List(element)
                asyncio.sleep(0)

    #data dejà modeliser depuis l'API distant
    async def __Fetch_Tour_Data_From_Database(self):
        result:ResponseFetch= requests.get("http://localhost:5000").json()
        await self.__Convert_Dict_Into_Class(result.get("data"))
    async def __Convert_Dict_Into_Class(self,element:Data):
        self.circuit.clear()
        self.adrenaline.clear()
        self.itineraire.clear()
        self.equipement_needed.clear()
        self.included.clear()
        for circuit,adrenaline,equipement,itinerary,included in zip_longest(element.get('circuit'),element.get("adrenaline"),element.get("equipment"),element.get("itinerary"),element.get("included_in_price"),fillvalue=None):
            if circuit:
                self.circuit.append(Circuit_Model(id=circuit.get("id"),title=circuit.get("title"),subtitle=circuit.get("subtitle"),description=circuit.get("description"),duration=circuit.get("duration"),difficulty=circuit.get("difficulty"),price=circuit.get("price"),image=circuit.get("image")))
            if adrenaline:
                self.adrenaline.append(Adrenaline_Model(id=adrenaline.get("id"),content=adrenaline.get("content"),circuit_id=adrenaline.get("circuit_id")))
            if itinerary:
                self.itineraire.append(Itinerary_Model(id=itinerary.get("id"),place=itinerary.get("place"),day=itinerary.get("day"),description=itinerary.get("description"),order_id=itinerary.get("order_id"),circuit_id=itinerary.get("circuit_id")))
            if equipement:
                self.equipement_needed.append(Equipement_Model(id=equipement.get("id"),equipment=equipement.get("equipment"),circuit_id=equipement.get("circuit_id")))
            if included:
                self.included.append(Included_task_in_Price_Model(id=included.get("id"),content=included.get("content"),circuit_id=included.get("circuit_id")))
            await asyncio.sleep(0)