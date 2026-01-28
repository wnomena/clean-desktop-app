import asyncio
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
        self.async_session = async_sessionmaker(self._engine,expire_on_commit=False) if self._engine else None
        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.submit(asyncio.run,self.Worker())
    
    async def Worker(self):
        while True:
            await self.__Fetch_Tour_Data_From_Database()
            await self.__Fetch_Contact_Data_From_Database()
            await asyncio.sleep(3600/2)
    
    async def __Append_To_Contact_List(self,contact:Contact):
        self.contact.clear()
        await self.contact.append(Contact_Model_without_Pydantic(id=contact.id,name=contact.name,subject=contact.subject,body=contact.body,mail=contact.mail,number=contact.number,begining=contact.begining,number_of_person=contact.number_of_person,circuit_id=contact.circuit_id,total_price=contact.total_price,Completed=contact.Completed))

    async def __Fetch_Contact_Data_From_Database(self):
        async with self.async_session() as session:
            get_data_in_join = select(Contact)
            for element in session.scalars(get_data_in_join):
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
                await self.circuit.append(Circuit_Model(id=circuit.get("id"),title=circuit.get("title"),subtitle=circuit.get("subtitle"),description=circuit.get("description"),duration=circuit.get("duration"),difficulty=circuit.get("difficulty"),price=circuit.get("price"),image=circuit.get("image")))
            if adrenaline:
                await self.adrenaline.append(Adrenaline_Model(id=adrenaline.get("id"),content=adrenaline.get("content"),circuit_id=adrenaline.get("circuit_id")))
            if itinerary:
                await self.itineraire.append(Itinerary_Model(id=itinerary.get("id"),place=itinerary.get("place"),order_id=itinerary.get("order_id"),circuit_id=itinerary.get("circuit_id")))
            if equipement:
                await self.equipement_needed.append(Equipement_Model(id=equipement.get("id"),equipment=equipement.get("equipment"),circuit_id=equipement.get("circuit_id")))
            if included:
                await self.included.append(Included_task_in_Price_Model(id=included.get("id"),content=included.get("content"),circuit_id=included.get("circuit_id")))
            await asyncio.sleep(0)