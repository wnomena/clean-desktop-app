from Model.SQLAlchemy.schema import Adrenaline_Model, Circuit_Model, Equipement_Model, Included_task_in_Price_Model, Itinerary_Model


class Temp_Data_During_Add_new_Circuit:
    #les données à proposer au client
    __adrenaline:list[Adrenaline_Model]  = []
    __itineraire:list[Itinerary_Model] = []
    __equipement_needed:list[Equipement_Model] = []
    __included:list[Included_task_in_Price_Model] = []

    #les nouveau données mise par le client
    new_circuit:list[Circuit_Model] = []
    new_adrenaline:list[Adrenaline_Model]  = []
    new_itineraire:list[Itinerary_Model] = []
    new_equipement_needed:list[Equipement_Model] = []
    new_included:list[Included_task_in_Price_Model] = []
    def __init__(self):
        pass
    
    def Inser_Data_In_One(self,adrenaline:list[Adrenaline_Model],itineraire:list[Itinerary_Model],equipement_needed:list[Equipement_Model],included:list[Included_task_in_Price_Model]):
        self.__adrenaline = adrenaline
        self.__itineraire = itineraire
        self.__equipement_needed = equipement_needed
        self.__included = included

    def GetAdrenalineList(self):
        return self.__adrenaline

    def GetItineraryList(self):
        return self.__itineraire
    
    def GetEquipementList(self):
        return self.__equipement_needed
    
    def GetIncludedList(self):
        return self.__included
    
    def Delete_Temp_Value(self):
        self.new_adrenaline = []
        self.new_circuit = []
        self.new_equipement_needed = []
        self.new_itineraire = []
        self.new_included = []