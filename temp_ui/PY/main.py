# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 490)
        MainWindow.setMinimumSize(QSize(900, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.circuits_ui = QWidget()
        self.circuits_ui.setObjectName(u"circuits_ui")
        self.verticalLayout_2 = QVBoxLayout(self.circuits_ui)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.circuits_ui)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.verticalLayout_2.addWidget(self.label)

        self.table_to_list_circuit = QTableView(self.circuits_ui)
        self.table_to_list_circuit.setObjectName(u"table_to_list_circuit")

        self.verticalLayout_2.addWidget(self.table_to_list_circuit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_add_new_tour = QPushButton(self.circuits_ui)
        self.btn_add_new_tour.setObjectName(u"btn_add_new_tour")
        self.btn_add_new_tour.setStyleSheet(u"background-color: rgb(46, 194, 126);")

        self.horizontalLayout.addWidget(self.btn_add_new_tour)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.circuits_ui)
        self.contact = QWidget()
        self.contact.setObjectName(u"contact")
        self.verticalLayout_4 = QVBoxLayout(self.contact)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.contact)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.table_to_list_contact = QTableView(self.contact)
        self.table_to_list_contact.setObjectName(u"table_to_list_contact")

        self.verticalLayout_4.addWidget(self.table_to_list_contact)

        self.stackedWidget.addWidget(self.contact)
        self.configuration_page = QWidget()
        self.configuration_page.setObjectName(u"configuration_page")
        self.verticalLayout_6 = QVBoxLayout(self.configuration_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.configuration_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(38, 162, 105);\n"
"")

        self.verticalLayout_5.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.configuration_page)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_7 = QLabel(self.configuration_page)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.database_name = QLineEdit(self.configuration_page)
        self.database_name.setObjectName(u"database_name")
        self.database_name.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.database_name, 2, 1, 1, 1)

        self.database_hosting = QLineEdit(self.configuration_page)
        self.database_hosting.setObjectName(u"database_hosting")
        self.database_hosting.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.database_hosting, 1, 1, 1, 1)

        self.label_5 = QLabel(self.configuration_page)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.database_port = QLineEdit(self.configuration_page)
        self.database_port.setObjectName(u"database_port")
        self.database_port.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.database_port, 5, 1, 1, 1)

        self.user_name = QLineEdit(self.configuration_page)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.user_name, 3, 1, 1, 1)

        self.database_password = QLineEdit(self.configuration_page)
        self.database_password.setObjectName(u"database_password")
        self.database_password.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.database_password, 4, 1, 1, 1)

        self.label_4 = QLabel(self.configuration_page)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_8 = QLabel(self.configuration_page)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btn_save_data_information = QPushButton(self.configuration_page)
        self.btn_save_data_information.setObjectName(u"btn_save_data_information")
        font1 = QFont()
        font1.setBold(False)
        self.btn_save_data_information.setFont(font1)
        self.btn_save_data_information.setStyleSheet(u"background-color: rgb(38, 162, 105);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.btn_save_data_information)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.configuration_page)
        self.add_circuit_page_1 = QWidget()
        self.add_circuit_page_1.setObjectName(u"add_circuit_page_1")
        self.verticalLayout_7 = QVBoxLayout(self.add_circuit_page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.add_circuit_page_1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_9)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.import_image_btn = QPushButton(self.add_circuit_page_1)
        self.import_image_btn.setObjectName(u"import_image_btn")

        self.gridLayout_2.addWidget(self.import_image_btn, 4, 3, 1, 2)

        self.circuit_price_input = QLineEdit(self.add_circuit_page_1)
        self.circuit_price_input.setObjectName(u"circuit_price_input")
        self.circuit_price_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.circuit_price_input, 4, 1, 1, 1)

        self.subtitle_input = QLineEdit(self.add_circuit_page_1)
        self.subtitle_input.setObjectName(u"subtitle_input")
        self.subtitle_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.subtitle_input, 3, 1, 1, 6)

        self.label_14 = QLabel(self.add_circuit_page_1)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)

        self.circuit_description_input = QPlainTextEdit(self.add_circuit_page_1)
        self.circuit_description_input.setObjectName(u"circuit_description_input")
        self.circuit_description_input.setStyleSheet(u"background-color: rgb(154, 153, 150);")

        self.gridLayout_2.addWidget(self.circuit_description_input, 6, 0, 1, 7)

        self.label_10 = QLabel(self.add_circuit_page_1)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_15 = QLabel(self.add_circuit_page_1)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 4, 2, 1, 1)

        self.label_17 = QLabel(self.add_circuit_page_1)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 5, 0, 1, 1)

        self.image_found_label = QLabel(self.add_circuit_page_1)
        self.image_found_label.setObjectName(u"image_found_label")

        self.gridLayout_2.addWidget(self.image_found_label, 4, 5, 1, 2)

        self.label_13 = QLabel(self.add_circuit_page_1)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)

        self.label_11 = QLabel(self.add_circuit_page_1)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.duration_day_input = QLineEdit(self.add_circuit_page_1)
        self.duration_day_input.setObjectName(u"duration_day_input")
        self.duration_day_input.setMinimumSize(QSize(50, 0))
        self.duration_day_input.setMaximumSize(QSize(100, 16777215))
        self.duration_day_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.duration_day_input, 2, 1, 1, 1)

        self.duration_night_input = QLineEdit(self.add_circuit_page_1)
        self.duration_night_input.setObjectName(u"duration_night_input")
        self.duration_night_input.setMinimumSize(QSize(50, 0))
        self.duration_night_input.setMaximumSize(QSize(100, 16777215))
        self.duration_night_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.duration_night_input, 2, 2, 1, 1)

        self.label_12 = QLabel(self.add_circuit_page_1)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 2, 3, 1, 1)

        self.circuit_title_input = QLineEdit(self.add_circuit_page_1)
        self.circuit_title_input.setObjectName(u"circuit_title_input")
        self.circuit_title_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.circuit_title_input, 1, 1, 1, 6)

        self.difficulty_input = QLineEdit(self.add_circuit_page_1)
        self.difficulty_input.setObjectName(u"difficulty_input")
        self.difficulty_input.setMinimumSize(QSize(100, 0))
        self.difficulty_input.setMaximumSize(QSize(10000, 16777215))
        self.difficulty_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.difficulty_input, 2, 4, 1, 3)


        self.verticalLayout_7.addLayout(self.gridLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.cancel_btn = QPushButton(self.add_circuit_page_1)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setStyleSheet(u"background-color: rgb(224, 27, 36);")

        self.horizontalLayout_4.addWidget(self.cancel_btn)

        self.btn_to_the_next_step_tool_for_travel = QPushButton(self.add_circuit_page_1)
        self.btn_to_the_next_step_tool_for_travel.setObjectName(u"btn_to_the_next_step_tool_for_travel")
        self.btn_to_the_next_step_tool_for_travel.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_4.addWidget(self.btn_to_the_next_step_tool_for_travel)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.add_circuit_page_1)
        self.add_circuit_page_2 = QWidget()
        self.add_circuit_page_2.setObjectName(u"add_circuit_page_2")
        self.verticalLayout_8 = QVBoxLayout(self.add_circuit_page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_16 = QLabel(self.add_circuit_page_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_16)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_18 = QLabel(self.add_circuit_page_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_18)

        self.add_new_tool_input = QLineEdit(self.add_circuit_page_2)
        self.add_new_tool_input.setObjectName(u"add_new_tool_input")
        self.add_new_tool_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.add_new_tool_input)

        self.new_tool_input_validation_btn = QPushButton(self.add_circuit_page_2)
        self.new_tool_input_validation_btn.setObjectName(u"new_tool_input_validation_btn")
        self.new_tool_input_validation_btn.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_5.addWidget(self.new_tool_input_validation_btn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_19 = QLabel(self.add_circuit_page_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_20 = QLabel(self.add_circuit_page_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 0, 1, 1, 1)

        self.table_view_to_list_old_tool = QTableView(self.add_circuit_page_2)
        self.table_view_to_list_old_tool.setObjectName(u"table_view_to_list_old_tool")

        self.gridLayout_4.addWidget(self.table_view_to_list_old_tool, 1, 0, 1, 1)

        self.table_view_to_list_all_tool_for_new_tour = QTableView(self.add_circuit_page_2)
        self.table_view_to_list_all_tool_for_new_tour.setObjectName(u"table_view_to_list_all_tool_for_new_tour")

        self.gridLayout_4.addWidget(self.table_view_to_list_all_tool_for_new_tour, 1, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.btn_cancel_processus = QPushButton(self.add_circuit_page_2)
        self.btn_cancel_processus.setObjectName(u"btn_cancel_processus")
        self.btn_cancel_processus.setStyleSheet(u"background-color: rgb(224, 27, 36);")

        self.horizontalLayout_6.addWidget(self.btn_cancel_processus)

        self.btn_back_to_first_page_adding_tour = QPushButton(self.add_circuit_page_2)
        self.btn_back_to_first_page_adding_tour.setObjectName(u"btn_back_to_first_page_adding_tour")
        self.btn_back_to_first_page_adding_tour.setStyleSheet(u"background-color: rgb(198, 70, 0);")

        self.horizontalLayout_6.addWidget(self.btn_back_to_first_page_adding_tour)

        self.btn_to_the_next_step_adrenaline = QPushButton(self.add_circuit_page_2)
        self.btn_to_the_next_step_adrenaline.setObjectName(u"btn_to_the_next_step_adrenaline")
        self.btn_to_the_next_step_adrenaline.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_6.addWidget(self.btn_to_the_next_step_adrenaline)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.add_circuit_page_2)
        self.add_circuit_page_3 = QWidget()
        self.add_circuit_page_3.setObjectName(u"add_circuit_page_3")
        self.verticalLayout_9 = QVBoxLayout(self.add_circuit_page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_21 = QLabel(self.add_circuit_page_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_9.addWidget(self.label_21)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_22 = QLabel(self.add_circuit_page_3)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_7.addWidget(self.label_22)

        self.add_new_adrenaline_input = QLineEdit(self.add_circuit_page_3)
        self.add_new_adrenaline_input.setObjectName(u"add_new_adrenaline_input")
        self.add_new_adrenaline_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.add_new_adrenaline_input)

        self.btn_to_add_new_adrenaline_for_this_tour = QPushButton(self.add_circuit_page_3)
        self.btn_to_add_new_adrenaline_for_this_tour.setObjectName(u"btn_to_add_new_adrenaline_for_this_tour")
        self.btn_to_add_new_adrenaline_for_this_tour.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_7.addWidget(self.btn_to_add_new_adrenaline_for_this_tour)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_24 = QLabel(self.add_circuit_page_3)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_3.addWidget(self.label_24, 0, 1, 1, 1)

        self.table_view_to_list_all_new_adrenaline_for_new_tour = QTableView(self.add_circuit_page_3)
        self.table_view_to_list_all_new_adrenaline_for_new_tour.setObjectName(u"table_view_to_list_all_new_adrenaline_for_new_tour")

        self.gridLayout_3.addWidget(self.table_view_to_list_all_new_adrenaline_for_new_tour, 1, 1, 1, 1)

        self.table_view_to_list_adrenaline = QTableView(self.add_circuit_page_3)
        self.table_view_to_list_adrenaline.setObjectName(u"table_view_to_list_adrenaline")

        self.gridLayout_3.addWidget(self.table_view_to_list_adrenaline, 1, 0, 1, 1)

        self.label_23 = QLabel(self.add_circuit_page_3)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 0, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.btn_cancel_processus_5 = QPushButton(self.add_circuit_page_3)
        self.btn_cancel_processus_5.setObjectName(u"btn_cancel_processus_5")
        self.btn_cancel_processus_5.setStyleSheet(u"background-color: rgb(224, 27, 36);")

        self.horizontalLayout_8.addWidget(self.btn_cancel_processus_5)

        self.btn_to_the_last_step_tool = QPushButton(self.add_circuit_page_3)
        self.btn_to_the_last_step_tool.setObjectName(u"btn_to_the_last_step_tool")
        self.btn_to_the_last_step_tool.setStyleSheet(u"background-color: rgb(198, 70, 0);")

        self.horizontalLayout_8.addWidget(self.btn_to_the_last_step_tool)

        self.btn_to_the_next_step_itinerary = QPushButton(self.add_circuit_page_3)
        self.btn_to_the_next_step_itinerary.setObjectName(u"btn_to_the_next_step_itinerary")
        self.btn_to_the_next_step_itinerary.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_8.addWidget(self.btn_to_the_next_step_itinerary)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.stackedWidget.addWidget(self.add_circuit_page_3)
        self.add_circuit_page_4 = QWidget()
        self.add_circuit_page_4.setObjectName(u"add_circuit_page_4")
        self.verticalLayout_10 = QVBoxLayout(self.add_circuit_page_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_25 = QLabel(self.add_circuit_page_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.verticalLayout_10.addWidget(self.label_25)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.sejours_delay_for_itinerary_input = QLineEdit(self.add_circuit_page_4)
        self.sejours_delay_for_itinerary_input.setObjectName(u"sejours_delay_for_itinerary_input")
        self.sejours_delay_for_itinerary_input.setMaximumSize(QSize(100, 16777215))
        self.sejours_delay_for_itinerary_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.sejours_delay_for_itinerary_input, 0, 4, 1, 1)

        self.label_29 = QLabel(self.add_circuit_page_4)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_5.addWidget(self.label_29, 2, 0, 1, 1)

        self.label_28 = QLabel(self.add_circuit_page_4)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 1, 0, 1, 1)

        self.itinerary_name_input = QLineEdit(self.add_circuit_page_4)
        self.itinerary_name_input.setObjectName(u"itinerary_name_input")
        self.itinerary_name_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.itinerary_name_input, 0, 2, 1, 1)

        self.table_view_to_list_itinerary_for_the_new_travel = QTableView(self.add_circuit_page_4)
        self.table_view_to_list_itinerary_for_the_new_travel.setObjectName(u"table_view_to_list_itinerary_for_the_new_travel")
        self.table_view_to_list_itinerary_for_the_new_travel.setStyleSheet(u"background-color: rgb(154, 153, 150);")

        self.gridLayout_5.addWidget(self.table_view_to_list_itinerary_for_the_new_travel, 3, 0, 1, 5)

        self.label_27 = QLabel(self.add_circuit_page_4)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 0, 3, 1, 1)

        self.itinerary_description_input = QLineEdit(self.add_circuit_page_4)
        self.itinerary_description_input.setObjectName(u"itinerary_description_input")
        self.itinerary_description_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.itinerary_description_input, 1, 1, 1, 4)

        self.label_26 = QLabel(self.add_circuit_page_4)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 0, 0, 1, 1)

        self.btn_add_new_itinerary = QPushButton(self.add_circuit_page_4)
        self.btn_add_new_itinerary.setObjectName(u"btn_add_new_itinerary")
        self.btn_add_new_itinerary.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.gridLayout_5.addWidget(self.btn_add_new_itinerary, 2, 3, 1, 2)


        self.verticalLayout_10.addLayout(self.gridLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.btn_cancel_processus_4 = QPushButton(self.add_circuit_page_4)
        self.btn_cancel_processus_4.setObjectName(u"btn_cancel_processus_4")
        self.btn_cancel_processus_4.setStyleSheet(u"background-color: rgb(224, 27, 36);")

        self.horizontalLayout_9.addWidget(self.btn_cancel_processus_4)

        self.btn_to_the_last_step_adrenaline = QPushButton(self.add_circuit_page_4)
        self.btn_to_the_last_step_adrenaline.setObjectName(u"btn_to_the_last_step_adrenaline")
        self.btn_to_the_last_step_adrenaline.setStyleSheet(u"background-color: rgb(198, 70, 0);\n"
"")

        self.horizontalLayout_9.addWidget(self.btn_to_the_last_step_adrenaline)

        self.btn_to_the_next_step_included_in_price = QPushButton(self.add_circuit_page_4)
        self.btn_to_the_next_step_included_in_price.setObjectName(u"btn_to_the_next_step_included_in_price")
        self.btn_to_the_next_step_included_in_price.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_9.addWidget(self.btn_to_the_next_step_included_in_price)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.stackedWidget.addWidget(self.add_circuit_page_4)
        self.add_circuit_page_5 = QWidget()
        self.add_circuit_page_5.setObjectName(u"add_circuit_page_5")
        self.verticalLayout_11 = QVBoxLayout(self.add_circuit_page_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_30 = QLabel(self.add_circuit_page_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.verticalLayout_11.addWidget(self.label_30)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_31 = QLabel(self.add_circuit_page_5)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_10.addWidget(self.label_31)

        self.add_new_task_onput = QLineEdit(self.add_circuit_page_5)
        self.add_new_task_onput.setObjectName(u"add_new_task_onput")
        self.add_new_task_onput.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.add_new_task_onput)

        self.btn_to_add_new_task = QPushButton(self.add_circuit_page_5)
        self.btn_to_add_new_task.setObjectName(u"btn_to_add_new_task")
        self.btn_to_add_new_task.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_10.addWidget(self.btn_to_add_new_task)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_32 = QLabel(self.add_circuit_page_5)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_6.addWidget(self.label_32, 0, 0, 1, 1)

        self.label_33 = QLabel(self.add_circuit_page_5)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_6.addWidget(self.label_33, 0, 1, 1, 1)

        self.tabke_view_list_of_existant_task = QTableView(self.add_circuit_page_5)
        self.tabke_view_list_of_existant_task.setObjectName(u"tabke_view_list_of_existant_task")

        self.gridLayout_6.addWidget(self.tabke_view_list_of_existant_task, 1, 0, 1, 1)

        self.table_view_to_list_task_for_new_travel = QTableView(self.add_circuit_page_5)
        self.table_view_to_list_task_for_new_travel.setObjectName(u"table_view_to_list_task_for_new_travel")

        self.gridLayout_6.addWidget(self.table_view_to_list_task_for_new_travel, 1, 1, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.btn_cancel_processus_2 = QPushButton(self.add_circuit_page_5)
        self.btn_cancel_processus_2.setObjectName(u"btn_cancel_processus_2")
        self.btn_cancel_processus_2.setStyleSheet(u"background-color: rgb(224, 27, 36);")

        self.horizontalLayout_11.addWidget(self.btn_cancel_processus_2)

        self.btn_to_last_step_itinerary = QPushButton(self.add_circuit_page_5)
        self.btn_to_last_step_itinerary.setObjectName(u"btn_to_last_step_itinerary")
        self.btn_to_last_step_itinerary.setStyleSheet(u"background-color: rgb(198, 70, 0);")

        self.horizontalLayout_11.addWidget(self.btn_to_last_step_itinerary)

        self.btn_to_next_step_resume_and_validation = QPushButton(self.add_circuit_page_5)
        self.btn_to_next_step_resume_and_validation.setObjectName(u"btn_to_next_step_resume_and_validation")
        self.btn_to_next_step_resume_and_validation.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_11.addWidget(self.btn_to_next_step_resume_and_validation)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.stackedWidget.addWidget(self.add_circuit_page_5)
        self.add_circuit_page_6_and_final = QWidget()
        self.add_circuit_page_6_and_final.setObjectName(u"add_circuit_page_6_and_final")
        self.verticalLayout_12 = QVBoxLayout(self.add_circuit_page_6_and_final)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_34 = QLabel(self.add_circuit_page_6_and_final)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_34)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.title_of_travel_label_validation = QLabel(self.add_circuit_page_6_and_final)
        self.title_of_travel_label_validation.setObjectName(u"title_of_travel_label_validation")
        self.title_of_travel_label_validation.setMaximumSize(QSize(200, 16777215))
        self.title_of_travel_label_validation.setFont(font)
        self.title_of_travel_label_validation.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.title_of_travel_label_validation)

        self.travel_subtitle_label_validation = QLabel(self.add_circuit_page_6_and_final)
        self.travel_subtitle_label_validation.setObjectName(u"travel_subtitle_label_validation")

        self.horizontalLayout_12.addWidget(self.travel_subtitle_label_validation)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.label_37 = QLabel(self.add_circuit_page_6_and_final)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)
        self.label_37.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_37)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_for_price_validation = QLabel(self.add_circuit_page_6_and_final)
        self.label_for_price_validation.setObjectName(u"label_for_price_validation")
        self.label_for_price_validation.setFont(font)
        self.label_for_price_validation.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_for_price_validation)

        self.duration_labeel_validation = QLabel(self.add_circuit_page_6_and_final)
        self.duration_labeel_validation.setObjectName(u"duration_labeel_validation")
        self.duration_labeel_validation.setFont(font)
        self.duration_labeel_validation.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.duration_labeel_validation)

        self.difficulty_label_validation = QLabel(self.add_circuit_page_6_and_final)
        self.difficulty_label_validation.setObjectName(u"difficulty_label_validation")
        self.difficulty_label_validation.setFont(font)
        self.difficulty_label_validation.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.difficulty_label_validation)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.label_35 = QLabel(self.add_circuit_page_6_and_final)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_35)

        self.description_text_edit_validation = QPlainTextEdit(self.add_circuit_page_6_and_final)
        self.description_text_edit_validation.setObjectName(u"description_text_edit_validation")
        self.description_text_edit_validation.setPlainText(u"Lorem ipsum is a dummy or placeholder text commonly used in graphic design, publishing, and web development. Its purpose is to permit a page layout to be designed, independently of the copy that will subsequently populate it")

        self.verticalLayout_12.addWidget(self.description_text_edit_validation)

        self.label_41 = QLabel(self.add_circuit_page_6_and_final)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)
        self.label_41.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_41)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_43 = QLabel(self.add_circuit_page_6_and_final)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)

        self.gridLayout_7.addWidget(self.label_43, 0, 1, 1, 1)

        self.label_44 = QLabel(self.add_circuit_page_6_and_final)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font)

        self.gridLayout_7.addWidget(self.label_44, 0, 0, 1, 1)

        self.label_42 = QLabel(self.add_circuit_page_6_and_final)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font)

        self.gridLayout_7.addWidget(self.label_42, 0, 2, 1, 1)

        self.tool_table_view_validation = QTableView(self.add_circuit_page_6_and_final)
        self.tool_table_view_validation.setObjectName(u"tool_table_view_validation")

        self.gridLayout_7.addWidget(self.tool_table_view_validation, 1, 0, 1, 1)

        self.adrenaline_table_view_validation = QTableWidget(self.add_circuit_page_6_and_final)
        self.adrenaline_table_view_validation.setObjectName(u"adrenaline_table_view_validation")

        self.gridLayout_7.addWidget(self.adrenaline_table_view_validation, 1, 1, 1, 1)

        self.included_table_view_validation = QTableView(self.add_circuit_page_6_and_final)
        self.included_table_view_validation.setObjectName(u"included_table_view_validation")

        self.gridLayout_7.addWidget(self.included_table_view_validation, 1, 2, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)

        self.btn_cancel_processus_3 = QPushButton(self.add_circuit_page_6_and_final)
        self.btn_cancel_processus_3.setObjectName(u"btn_cancel_processus_3")
        self.btn_cancel_processus_3.setStyleSheet(u"background-color: rgb(224, 27, 36);")

        self.horizontalLayout_14.addWidget(self.btn_cancel_processus_3)

        self.btn_back_to_the_last_step_included = QPushButton(self.add_circuit_page_6_and_final)
        self.btn_back_to_the_last_step_included.setObjectName(u"btn_back_to_the_last_step_included")
        self.btn_back_to_the_last_step_included.setStyleSheet(u"background-color: rgb(255, 120, 0);")

        self.horizontalLayout_14.addWidget(self.btn_back_to_the_last_step_included)

        self.btn_validation_and_commit_to_database = QPushButton(self.add_circuit_page_6_and_final)
        self.btn_validation_and_commit_to_database.setObjectName(u"btn_validation_and_commit_to_database")
        self.btn_validation_and_commit_to_database.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_14.addWidget(self.btn_validation_and_commit_to_database)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.stackedWidget.addWidget(self.add_circuit_page_6_and_final)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 0))
        self.widget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tours_btn = QPushButton(self.widget)
        self.tours_btn.setObjectName(u"tours_btn")
        self.tours_btn.setStyleSheet(u"background-color: rgb(28, 113, 216);")

        self.verticalLayout.addWidget(self.tours_btn)

        self.contact_btn = QPushButton(self.widget)
        self.contact_btn.setObjectName(u"contact_btn")
        self.contact_btn.setStyleSheet(u"background-color: rgb(28, 113, 216);")

        self.verticalLayout.addWidget(self.contact_btn)

        self.config_btn = QPushButton(self.widget)
        self.config_btn.setObjectName(u"config_btn")
        self.config_btn.setStyleSheet(u"background-color: rgb(28, 113, 216);")

        self.verticalLayout.addWidget(self.config_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Madagascar-Tours", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Circuits", None))
        self.btn_add_new_tour.setText(QCoreApplication.translate("MainWindow", u"Ajouter de nouveau circuit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Mots de passe pour la base de donn\u00e9es", None))
        self.database_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"local_caponmada", None))
        self.database_hosting.setPlaceholderText(QCoreApplication.translate("MainWindow", u"caponmada.mg/192.168.1.1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nom de base de donn\u00e9es", None))
        self.database_port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"3306", None))
        self.user_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"root", None))
        self.database_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"root", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Adresse de la base de donn\u00e9es", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Numero de port", None))
        self.btn_save_data_information.setText(QCoreApplication.translate("MainWindow", u"Enregistrer les modifications", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ajout de nouveau circuit", None))
        self.import_image_btn.setText(QCoreApplication.translate("MainWindow", u"Importer une image", None))
        self.circuit_price_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.subtitle_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Une petite phrase comme presentation du circuit", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Prix", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nom de circuit", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Images", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.image_found_label.setText(QCoreApplication.translate("MainWindow", u"Aucune image trouv\u00e9e", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Sous-titre", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Dur\u00e9e du voyage", None))
        self.duration_day_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Jours", None))
        self.duration_night_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nuit", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Difficult\u00e9", None))
        self.circuit_title_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Zoo de Tsimbazaza", None))
        self.difficulty_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"100", None))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.btn_to_the_next_step_tool_for_travel.setText(QCoreApplication.translate("MainWindow", u"aller \u00e0 la page suivante", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Equipement utile lors du trajet", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Ajouter un nouvel \u00e9quipement", None))
        self.add_new_tool_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Une p\u00e8le", None))
        self.new_tool_input_validation_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Liste des \u00e9quipements des autres trajets", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Les \u00e9quipements pour le nouveau trajet", None))
        self.btn_cancel_processus.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.btn_back_to_first_page_adding_tour.setText(QCoreApplication.translate("MainWindow", u"Revenir vers la pr\u00e9c\u00e9dente page", None))
        self.btn_to_the_next_step_adrenaline.setText(QCoreApplication.translate("MainWindow", u"Passer \u00e0 la page suivante", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Les points forts du trajet", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Ajouter un nouveau point fort pour ce trajet", None))
        self.add_new_adrenaline_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Le septiemme ciel", None))
        self.btn_to_add_new_adrenaline_for_this_tour.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Les adrenalines pour le nouveau circuit", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Liste des adrenalines dispo", None))
        self.btn_cancel_processus_5.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.btn_to_the_last_step_tool.setText(QCoreApplication.translate("MainWindow", u"Revenir \u00e0 la page pr\u00e9c\u00e9dente", None))
        self.btn_to_the_next_step_itinerary.setText(QCoreApplication.translate("MainWindow", u"Passer \u00e0 la page suivante", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Ajout des itineraires pour ce trajet", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"La liste de ceux pour ce trajet", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"dur\u00e9e de s\u00e9jours", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Nom de l'endroit", None))
        self.btn_add_new_itinerary.setText(QCoreApplication.translate("MainWindow", u"Ajouter un nouveau", None))
        self.btn_cancel_processus_4.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.btn_to_the_last_step_adrenaline.setText(QCoreApplication.translate("MainWindow", u"Revenir \u00e0 la page pr\u00e9c\u00e9dente", None))
        self.btn_to_the_next_step_included_in_price.setText(QCoreApplication.translate("MainWindow", u"Passer \u00e0 la page suivante", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Les taches incluses dans le prix du trajet", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Ajout d'une nouvelle tache pour le trajet", None))
        self.btn_to_add_new_task.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Liste des taches existantes", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Liste des taches pour le nouveau trajet", None))
        self.btn_cancel_processus_2.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.btn_to_last_step_itinerary.setText(QCoreApplication.translate("MainWindow", u"Revenir sur la page pr\u00e9cedente", None))
        self.btn_to_next_step_resume_and_validation.setText(QCoreApplication.translate("MainWindow", u"Terminer l'ajout du circuit", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9sentation du circuit", None))
        self.title_of_travel_label_validation.setText(QCoreApplication.translate("MainWindow", u"Zoo de Tsimazaza", None))
        self.travel_subtitle_label_validation.setText(QCoreApplication.translate("MainWindow", u"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical ,....", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"D\u00e9tails techniques", None))
        self.label_for_price_validation.setText(QCoreApplication.translate("MainWindow", u"500 E", None))
        self.duration_labeel_validation.setText(QCoreApplication.translate("MainWindow", u"5 jours / 5 nuits", None))
        self.difficulty_label_validation.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Autres informations", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Moments forts du trajet", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Equipements n\u00e9cessaires", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Inclus dans le prix", None))
        self.btn_cancel_processus_3.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.btn_back_to_the_last_step_included.setText(QCoreApplication.translate("MainWindow", u"Revenir", None))
        self.btn_validation_and_commit_to_database.setText(QCoreApplication.translate("MainWindow", u"Valider et terminer", None))
        self.tours_btn.setText(QCoreApplication.translate("MainWindow", u"Circuits", None))
        self.contact_btn.setText(QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.config_btn.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
    # retranslateUi

