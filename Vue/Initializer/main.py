from Model.Getter_Model.GetterOfAllInfoFromDatabase import Instance_of_All_Data
from Vue.Model_For_Table_View.Adrenaline_model import Adrenaline_Modeliser_For_TableView
from Vue.Model_For_Table_View.Equipement_model import Equipement_Modeliser_For_TableView
from Vue.Model_For_Table_View.Included_model import Included_Modeliser_For_TableView
from Vue.Model_For_Table_View.circuit_list_model import Tour_Modeliser_For_Table_View
from temp_ui.PY.main import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow





class Final():
    __all_data_instance = Instance_of_All_Data()
    __adrenaline_model = Adrenaline_Modeliser_For_TableView()
    __circuit_model = Tour_Modeliser_For_Table_View()
    __equipement_model = Equipement_Modeliser_For_TableView()
    __included_model = Included_Modeliser_For_TableView()




    __Client_ui = Ui_MainWindow()

    def __init__(self,window:QMainWindow):
        self.__adrenaline_model.Add_All_Data(self.__all_data_instance.adrenaline)
        self.__circuit_model.Add_All_Data(self.__all_data_instance.circuit)
        self.__equipement_model.Add_All_Data(self.__all_data_instance.equipement_needed)
        self.__included_model.Add_All_Data(self.__all_data_instance.included)
        self.__Client_ui.setupUi(window)
        self.__Client_ui.table_to_list_circuit.setModel(self.__circuit_model.Ready_Model())

    

    



