from functools import partial
from Model.Getter_Model.GetterOfAllInfoFromDatabase import Instance_of_All_Data
from Model.Pool import Getter_For_Txt_File
from Vue.Model_For_Table_View.Adrenaline_model import Adrenaline_Modeliser_For_TableView
from Vue.Model_For_Table_View.Equipement_model import Equipement_Modeliser_For_TableView
from Vue.Model_For_Table_View.Included_model import Included_Modeliser_For_TableView
from Vue.Model_For_Table_View.circuit_list_model import Tour_Modeliser_For_Table_View
from Vue.Model_For_Table_View.contact_list_model import Contact_Modeliser_For_TableView
from temp_ui.PY.main import Ui_MainWindow
from temp_ui.PY.add_tour_dialog import Ui_Magadagascar_Tours
from PySide6.QtWidgets import QMainWindow,QHeaderView





class Final():

    __DataBase_Verification = Getter_For_Txt_File()
    __adrenaline_model = Adrenaline_Modeliser_For_TableView()
    __circuit_model = Tour_Modeliser_For_Table_View()
    __equipement_model = Equipement_Modeliser_For_TableView()
    __included_model = Included_Modeliser_For_TableView()
    __contact_model = Contact_Modeliser_For_TableView()
    __Client_ui = Ui_MainWindow()
    __Dialog_For_New_Tour = Ui_Magadagascar_Tours()
    
    def changement_de_page(self,index:int):
        self.__Client_ui.stackedWidget.setCurrentIndex(index)
    def __init__(self,window:QMainWindow):
        if self.__DataBase_Verification.initaliser():
            self.__all_data_instance = Instance_of_All_Data()
            self.__adrenaline_model.Add_All_Data(self.__all_data_instance.adrenaline)
            self.__circuit_model.Add_All_Data(circuit=self.__all_data_instance.circuit)
            self.__equipement_model.Add_All_Data(self.__all_data_instance.equipement_needed)
            self.__included_model.Add_All_Data(self.__all_data_instance.included)
            self.__contact_model.Add_All_Data(self.__all_data_instance.contact)
            header_table_circuit = self.__Client_ui.table_to_list_circuit.horizontalHeader()
            header_table_contact = self.__Client_ui.table_to_list_contact.horizontalHeader()
            header_table_circuit.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            header_table_contact.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.__Client_ui.table_to_list_circuit.setModel(self.__circuit_model.Ready_Model())
            self.__Client_ui.table_to_list_contact.setModel(self.__contact_model.Ready_Model())
        self.__Client_ui.setupUi(window)
        if self.__DataBase_Verification.initaliser() is False:
            self.changement_de_page(0)
            self.__Client_ui.btn_save_data_information.clicked.connect(lambda:self.ajout_de_donnees_de_connexion())
        self.__Client_ui.contact_btn.clicked.connect(lambda:self.changement_de_page(2))
        self.__Client_ui.config_btn.clicked.connect(lambda:self.changement_de_page(0))
        self.__Client_ui.tours_btn.clicked.connect(lambda:self.changement_de_page(1))

    def ajout_de_donnees_de_connexion(self):
        with open("database_info.txt","w") as file:
            file.write(f"{self.__Client_ui.database_hosting.text()},{self.__Client_ui.database_name.text()},{self.__Client_ui.user_name.text()},{self.__Client_ui.database_password.text()},{self.__Client_ui.database_port.text()}")      



