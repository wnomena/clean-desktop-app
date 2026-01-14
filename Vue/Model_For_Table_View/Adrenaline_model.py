from PySide6.QtGui import QStandardItemModel,QStandardItem
from Model.SQLAlchemy.schema import Adrenaline_Model


class Adrenaline_Modeliser_For_TableView:
    def Add_All_Data(self,adrenaline:list[Adrenaline_Model]):
        self.header = ["Element"]
        self.data = [element.content for element in adrenaline]
        
    def Ready_Model(self) -> QStandardItemModel:
        model = QStandardItemModel()
        model.setRowCount(len(self.data))
        model.setColumnCount(len(self.header))
        for key,element in enumerate(self.data):
            item = QStandardItem(element)
            model.setItem(0,key,item)
        return model