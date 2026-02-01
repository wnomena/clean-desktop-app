from functools import partial
import os
import time
from typing import Dict
from Model.Getter_Model.GetterOfAllInfoFromDatabase import Instance_of_All_Data
from Model.Pool import Getter_For_Txt_File
from Model.SQLAlchemy.schema import Circuit_Model, Itinerary_Model
from Presenter.Action_On_The_View_By_User.Temp import Temp_Data_During_Add_new_Circuit
from Vue.Model_For_Table_View.Adrenaline_model import Adrenaline_Modeliser_For_TableView
from Vue.Model_For_Table_View.Equipement_model import Equipement_Modeliser_For_TableView
from Vue.Model_For_Table_View.Included_model import Included_Modeliser_For_TableView
from Vue.Model_For_Table_View.circuit_list_model import Tour_Modeliser_For_Table_View
from Vue.Model_For_Table_View.contact_list_model import Contact_Modeliser_For_TableView
from Vue.Model_For_Table_View.itinerary_list_model import Itinerary_Modeliser_For_TableView
from temp_ui.PY.main import Ui_MainWindow
from temp_ui.PY.add_tour_dialog import Dialog, Ui_Magadagascar_Tours
from PySide6.QtWidgets import QMainWindow,QHeaderView,QAbstractItemView,QFileDialog
from PySide6.QtCore import Slot





class Final():

    __DataBase_Verification = Getter_For_Txt_File()
    __adrenaline_model = Adrenaline_Modeliser_For_TableView()
    __circuit_model = Tour_Modeliser_For_Table_View()
    __equipement_model = Equipement_Modeliser_For_TableView()
    __included_model = Included_Modeliser_For_TableView()
    __itinerary_model = Itinerary_Modeliser_For_TableView()
    __contact_model = Contact_Modeliser_For_TableView()
    __Client_ui = Ui_MainWindow()
    __Temp_Data_During_add_Circuit = Temp_Data_During_Add_new_Circuit()
    
    
    def changement_de_page(self,index:int):
        self.__Client_ui.stackedWidget.setCurrentIndex(index)
    def __init__(self,window:QMainWindow):
        self.window = window
        self.__Client_ui.setupUi(window)
        print(self.__DataBase_Verification.initaliser())
        if self.__DataBase_Verification.initaliser():
            self.data_migration()
        else:
            self.changement_de_page(0)
            self.__Client_ui.btn_save_data_information.clicked.connect(lambda:self.ajout_de_donnees_de_connexion())
        self.__Client_ui.contact_btn.clicked.connect(lambda:self.changement_de_page(1))
        self.__Client_ui.config_btn.clicked.connect(lambda:self.changement_de_page(2))
        self.__Client_ui.tours_btn.clicked.connect(lambda:self.changement_de_page(0))
        self.__Client_ui.btn_add_new_tour.clicked.connect(lambda:self.changement_de_page(3))
        self.__Client_ui.import_image_btn.clicked.connect(lambda:self.saveFileDialog())
        self.__Client_ui.btn_to_the_next_step_tool_for_travel.clicked.connect(lambda:self.navigation_for_page_2())
        self.__Client_ui.cancel_btn.clicked.connect(lambda:self.all_value_deletion())
        self.__Client_ui.btn_cancel_processus.clicked.connect(lambda:self.all_value_deletion())
        self.__Client_ui.btn_cancel_processus_2.clicked.connect(lambda:self.all_value_deletion())
        self.__Client_ui.btn_cancel_processus_3.clicked.connect(lambda:self.all_value_deletion())
        self.__Client_ui.btn_cancel_processus_4.clicked.connect(lambda:self.all_value_deletion())
        self.__Client_ui.btn_cancel_processus_5.clicked.connect(lambda:self.all_value_deletion())

    def data_migration(self):
        self.__all_data_instance = Instance_of_All_Data()
        print(self.__all_data_instance.contact)
        self.__adrenaline_model.Add_All_Data(self.__all_data_instance.adrenaline)
        self.__circuit_model.Add_All_Data(circuit=self.__all_data_instance.circuit)
        self.__equipement_model.Add_All_Data(self.__all_data_instance.equipement_needed)
        self.__included_model.Add_All_Data(self.__all_data_instance.included)
        self.__contact_model.Add_All_Data(self.__all_data_instance.contact)
        print(self.__contact_model.data)
        header_table_circuit = self.__Client_ui.table_to_list_circuit.horizontalHeader()
        header_table_contact = self.__Client_ui.table_to_list_contact.horizontalHeader()
        header_table_circuit.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header_table_contact.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.__Client_ui.table_to_list_circuit.setModel(self.__circuit_model.Ready_Model())
        self.__Client_ui.table_to_list_contact.setModel(self.__contact_model.Ready_Model())
        self.__Client_ui.table_to_list_circuit.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.__Client_ui.table_to_list_contact.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.__Client_ui.stackedWidget.setCurrentIndex(0)
    def ajout_de_donnees_de_connexion(self):
        with open("database_info.txt","w") as file:
            file.write(f"{self.__Client_ui.database_hosting.text()},{self.__Client_ui.database_name.text()},{self.__Client_ui.user_name.text()},{self.__Client_ui.database_password.text()},{self.__Client_ui.database_port.text()}")      
        self.data_migration()

    def navigation_for_page_2(self):
        try:
            title = str(self.__Client_ui.circuit_title_input.text())
            subtitle = str(self.__Client_ui.subtitle_input.text())
            price = int(self.__Client_ui.circuit_price_input.text())
            difficulty = int(self.__Client_ui.difficulty_input.text())
            duration_day = int(self.__Client_ui.duration_day_input.text())
            duration_night = int(self.__Client_ui.duration_night_input.text())
            description = self.__Client_ui.circuit_description_input.toPlainText()
            print(f"id=None,title={title},subtitle={subtitle},description={description},duration={duration_day} jours / {duration_night} nuits,difficulty={difficulty},price={price},image={self.temp_image}")
            if len(title) > 1 and len(subtitle) > 1 and price > 1 and difficulty > 1 and duration_day > 1 and  duration_night > 1 and len(description) > 1 and len(self.temp_image) > 5:
                self.__Temp_Data_During_add_Circuit.new_circuit = Circuit_Model(id=None,title=title,subtitle=subtitle,description=description,duration=f"{duration_day} jours / {duration_night} nuits",difficulty=difficulty,price=price,image=self.temp_image)
                print(self.__Temp_Data_During_add_Circuit.new_circuit)
                self.__Client_ui.stackedWidget.setCurrentIndex(4)
            else:
                pass
        except Exception:
            print("Exception")
            pass
    

    def validation_of_new_itinerary(self):
        itinerary_name = self.__Client_ui.itinerary_name_input.text()
        day_number = self.__Client_ui.sejours_delay_for_itinerary_input.text()
        description = self.__Client_ui.itinerary_description_input.text()
        try:
            if len(itinerary_name) > 1 and int(day_number) > 1 and len(description) > 1:
                self.__itinerary_model.Add_All_Data(Itinerary_Model(id=None,place=itinerary_name,order_id=None,circuit_id=None,description=description,day=int(day_number)))
                self.__Client_ui.itinerary_name_input.setText("")
                self.__Client_ui.sejours_delay_for_itinerary_input.setText("")
                self.__Client_ui.itinerary_description_input.setText("")
                self.__Client_ui.table_view_to_list_itinerary_for_the_new_travel.setModel(self.__itinerary_model.Ready_Model())
            else:
                pass
        except Exception:
            pass

    def saveFileDialog(self):
        print('mande va ?')
        file_dialog = QFileDialog(self.window)
        file_dialog.setWindowTitle("Save File")
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)

        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            self.temp_image = selected_file
            self.__Client_ui.image_found_label.setText(selected_file.split("/")[len(selected_file.split("/")) - 1])

    def all_value_deletion(self):
            #add element page 1 travel caracteristic
            self.__Client_ui.circuit_title_input.setText("")
            self.__Client_ui.subtitle_input.setText("")
            self.__Client_ui.circuit_price_input.setText("")
            self.__Client_ui.difficulty_input.setText("")
            self.__Client_ui.duration_day_input.setText("")
            self.__Client_ui.duration_night_input.setText("")
            self.__Client_ui.circuit_description_input.setPlainText("")
            self.__Client_ui.image_found_label.setText("Aucune image trouvé")
            #add element page 2 tool
            self.__equipement_model.Delete_All_temp()
            #add element page 3 adrenaline
            self.__adrenaline_model.Delete_All_temp()
            #add element page 4 itinerary
            self.__itinerary_model.Delete_All_temp()
            #add element page 5 included in price
            self.__included_model.Delete_All_temp()
            #there are no deletion for page 6 because it's juste a resume of these 5 pages
            self.__Temp_Data_During_add_Circuit.Delete_Temp_Value()
            self.__Client_ui.stackedWidget.setCurrentIndex(0)