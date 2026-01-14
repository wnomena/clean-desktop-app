from PySide6.QtGui import QStandardItemModel,QStandardItem
from Model.SQLAlchemy.schema import Equipement_Model


class Equipement_Modeliser_For_TableView:
    def Add_All_Data(self,equipment:list[Equipement_Model]):
        self.header = ["Element"]
        self.data = [element.equipment for element in equipment]
        
    def Ready_Model(self) -> QStandardItemModel:
        model = QStandardItemModel()
        model.setRowCount(len(self.data))
        model.setColumnCount(len(self.header))
        for key,element in enumerate(self.data):
            item = QStandardItem(element)
            model.setItem(0,key,item)
        return model