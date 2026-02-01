from Model.SQLAlchemy.schema import Itinerary_Model
from PySide6.QtGui import QStandardItemModel,QStandardItem


class Itinerary_Modeliser_For_TableView:
    data:list[Itinerary_Model] = []
    def __init__(self):
        pass

    def Add_All_Data(self,itinerary:Itinerary_Model): 
        self.header = ["Position","Nom de l'endroit","Durée de séjours"]
        self.data.append(itinerary)


    def Ready_Model(self) -> QStandardItemModel:
        model = QStandardItemModel()
        model.setRowCount(len(self.data) + 1)
        model.setColumnCount(len(self.header))
        for row_index in range(len(self.data) + 1):
            if row_index == 0:
                for key,element in enumerate(self.header):
                    item = QStandardItem(element)
                    model.setItem(row_index,key,item)
            else:
                position = QStandardItem(str(self.data[row_index - 1].order_id))
                itinerary_name = QStandardItem(self.data[row_index - 1].place)
                sejours_delay = QStandardItem(f"{self.data[row_index - 1].day}  jours")
                model.setItem(row_index,0,position)
                model.setItem(row_index,1,itinerary_name)
                model.setItem(row_index,2,sejours_delay)
        return model

    def Delete_All_temp(self):
        self.data = []