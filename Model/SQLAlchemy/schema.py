from typing import TypedDict
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase,relationship
from sqlalchemy import String,Integer,ForeignKey

class Base(DeclarativeBase):
    pass

class Circuit(Base):
    __tablename__ = "circuit"
    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(50),nullable=False)
    subtitle:Mapped[str] = mapped_column(String(250),nullable=False)
    description:Mapped[str] = mapped_column(String,nullable=False)
    duration:Mapped[str] = mapped_column(String,nullable=False)
    difficulty:Mapped[int] = mapped_column(Integer,nullable=False)
    price:Mapped[int] = mapped_column(Integer,nullable=False)
    image:Mapped[str] = mapped_column(String,nullable=False)
    itinerary = relationship("Itinerary",back_populates="circuit")
    equipment_needed = relationship("Equipement",back_populates="circuit")
    included_in_price = relationship("Included_task_in_Price",back_populates="circuit")
    contact = relationship("Contact",back_populates="circuit")
    adrenaline = relationship("Adrenaline",back_populates="circuit")

class Circuit_Model:
    def __init__(self,
        id:int | None,
        title:str,
        subtitle:str,
        description:str,
        duration:str,
        difficulty:int,
        price:int,
        image:str):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.duration = duration
        self.description = description
        self.difficulty = difficulty
        self.price = price
        self.image = image

    

class Itinerary(Base):
    __tablename__= "itinerary"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    place:Mapped[str] = mapped_column(String,nullable=False)
    order_id:Mapped[int] = mapped_column(Integer,nullable=False)
    circuit_id:Mapped[int] = mapped_column(Integer,ForeignKey("circuit.id"))
    circuit = relationship("Circuit",back_populates="itinerary")

class Itinerary_Model:
    def __init__(self,id:int | None,
    place:str,
    order_id:int,
    circuit_id:int):
        self.id = id
        self.place = place
        self.order_id = order_id
        self.circuit_id = circuit_id


class Equipement(Base):
    __tablename__= "equipment_needed"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    equipment:Mapped[str] = mapped_column(String,nullable=False)
    circuit_id:Mapped[int] = mapped_column(Integer,ForeignKey("circuit.id"))
    circuit = relationship("Circuit",back_populates="equipment_needed")

class Equipement_Model:
    def __init__(self,id:int | None,
    equipment:str,
    circuit_id:int):
        self.id = id
        self.equipment = equipment
        self.circuit_id = circuit_id

class Included_task_in_Price(Base):
    __tablename__= "included_in_price"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    content:Mapped[str] = mapped_column(String,nullable=False)
    circuit_id:Mapped[int] = mapped_column(Integer,ForeignKey("circuit.id"))
    circuit = relationship("Circuit",back_populates="included_in_price")

class Included_task_in_Price_Model:
    def __init__(self,id:int | None,
    content:str,
    circuit_id:int):
        self.id = id
        self.content = content
        self.circuit_id = circuit_id

class Adrenaline(Base):
    __tablename__= "adrenaline"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    content:Mapped[str] = mapped_column(String,nullable=False)
    circuit_id:Mapped[int] = mapped_column(Integer,ForeignKey("circuit.id"))
    circuit = relationship("Circuit",back_populates="adrenaline")

class Adrenaline_Model:
    def __init__(self,id:int | None,
    content:str,
    circuit_id:int):
        self.id = id
        self.content = content
        self.circuit_id = circuit_id



class Contact(Base):
    __tablename__ = "contact"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String,nullable=False)
    subject:Mapped[str] = mapped_column(String,nullable=True)
    body:Mapped[str] = mapped_column(String,nullable=False)
    number:Mapped[str] = mapped_column(String,nullable=True)
    mail:Mapped[str] = mapped_column(String(250),nullable=False)
    begining:Mapped[str] = mapped_column(String,nullable=True)
    number_of_person:Mapped[int] = mapped_column(Integer,nullable=True)
    total_price:Mapped[int] = mapped_column(Integer,nullable=True)
    circuit_id:Mapped[int] = mapped_column(Integer,ForeignKey("circuit.id"),nullable=True)
    Completed:Mapped[int] = mapped_column(Integer,default=1,nullable=False)
    circuit = relationship("Circuit",back_populates="contact")

class Contact_Model_without_Pydantic:
    def __init__(self,    id:int | None,
    name:str,
    subject:str | None,
    body:str,
    mail:str,
    number:str | None,
    begining:str | None,
    number_of_person:int | None,
    circuit_id:int | None,
    total_price:int | None,Completed:int | None):
        self.id = id
        self.name = name,
        self.subject = subject
        self.body = body
        self.mail = mail
        self.number = number
        self.begining = begining
        self.number_of_person = number_of_person
        self.total_price = total_price
        self.circuit_id = circuit_id
        self.Completed = Completed

    
class Circuit_Dict_Mode(TypedDict):
    id:int | None
    title:str
    subtitle:str
    description:str
    duration:str
    difficulty:int
    price:int
    image:str


class Itinerary_Dict_Mode(TypedDict):
    id:int | None
    place:str
    order_id:int
    circuit_id:int

class Equipement_Dicat_Mode(TypedDict):
    id:int | None
    equipment:str
    circuit_id:int

class Adrenaline_Dicat_Mode(TypedDict):
    id:int | None
    content:str
    circuit_id:int

class Included_Dicat_Mode(TypedDict):
    id:int | None
    content:str
    circuit_id:int

class Data(TypedDict):
    adrenaline:list[Adrenaline_Dicat_Mode]
    circuit:list[Circuit_Dict_Mode]
    included_in_price:list[Included_Dicat_Mode]
    equipment:list[Equipement_Dicat_Mode]
    itinerary:list[Itinerary_Dict_Mode]

class ResponseFetch(TypedDict):
    code:int
    data:Data
    error:str

