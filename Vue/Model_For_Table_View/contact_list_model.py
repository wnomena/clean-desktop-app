from PySide6.QtGui import QStandardItemModel,QStandardItem
from Model.SQLAlchemy.schema import Contact_Model_without_Pydantic

class Contact_Modeliser_For_TableView():
    def __init__(self):
        pass
    def Add_All_Data(self,contact:list[Contact_Model_without_Pydantic]):

        self.header = ["Identifiant","Nom du client","Adresse mail"]
        self.data = [[],[],[]]
        for key,element in enumerate(contact):
            if element.Completed:
                self.data[0].insert(key,element.id)
                self.data[1].insert(key,element.name)
                self.data[2].insert(key,element.mail)

        print(self.data)

    def Ready_Model(self) -> QStandardItemModel:
        model = QStandardItemModel()
        model.setColumnCount(len(self.header))
        model.setRowCount(len(self.data[0]))
        for index_row in range(len(self.data[0]) + 1 ):
            for index_column in range(len(self.header)):
                if index_row == 0:
                    item = QStandardItem(self.header[index_column])
                    model.setItem(index_row,index_column,item)
                elif index_row > 0:
                    item = QStandardItem(str(self.data[index_column][index_row - 1]))
                    model.setItem(index_row,index_column,item)

        return model