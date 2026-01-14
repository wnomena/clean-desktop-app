# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_tour.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_Magadagascar_Tours(object):
    def setupUi(self, Magadagascar_Tours):
        if not Magadagascar_Tours.objectName():
            Magadagascar_Tours.setObjectName(u"Magadagascar_Tours")
        Magadagascar_Tours.resize(901, 502)
        Magadagascar_Tours.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.verticalLayout = QVBoxLayout(Magadagascar_Tours)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(Magadagascar_Tours)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font = QFont()
        font.setBold(True)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(192, 191, 188);\n"
"\n"
"")
        self.home_page_to_add_tour = QWidget()
        self.home_page_to_add_tour.setObjectName(u"home_page_to_add_tour")
        self.verticalLayout_2 = QVBoxLayout(self.home_page_to_add_tour)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.home_page_to_add_tour)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.input_for_night_number_for_travel = QLineEdit(self.home_page_to_add_tour)
        self.input_for_night_number_for_travel.setObjectName(u"input_for_night_number_for_travel")
        self.input_for_night_number_for_travel.setMinimumSize(QSize(100, 0))
        self.input_for_night_number_for_travel.setMaximumSize(QSize(100, 16777215))
        self.input_for_night_number_for_travel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.input_for_night_number_for_travel, 0, 4, 1, 1)

        self.label_7 = QLabel(self.home_page_to_add_tour)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 2, 1, 1)

        self.input_for_day_number_for_travel = QLineEdit(self.home_page_to_add_tour)
        self.input_for_day_number_for_travel.setObjectName(u"input_for_day_number_for_travel")
        self.input_for_day_number_for_travel.setMinimumSize(QSize(100, 0))
        self.input_for_day_number_for_travel.setMaximumSize(QSize(100, 16777215))
        self.input_for_day_number_for_travel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.input_for_day_number_for_travel, 0, 3, 1, 1)

        self.Btn_for_choosing_file = QPushButton(self.home_page_to_add_tour)
        self.Btn_for_choosing_file.setObjectName(u"Btn_for_choosing_file")

        self.gridLayout.addWidget(self.Btn_for_choosing_file, 3, 3, 1, 1)

        self.input_for_price_of_travel = QLineEdit(self.home_page_to_add_tour)
        self.input_for_price_of_travel.setObjectName(u"input_for_price_of_travel")
        self.input_for_price_of_travel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.input_for_price_of_travel, 3, 1, 1, 1)

        self.label_5 = QLabel(self.home_page_to_add_tour)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_3 = QLabel(self.home_page_to_add_tour)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_4 = QLabel(self.home_page_to_add_tour)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 5, 1, 1)

        self.input_for_little_description_of_travel = QLineEdit(self.home_page_to_add_tour)
        self.input_for_little_description_of_travel.setObjectName(u"input_for_little_description_of_travel")
        self.input_for_little_description_of_travel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.input_for_little_description_of_travel, 2, 1, 1, 6)

        self.label_2 = QLabel(self.home_page_to_add_tour)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.input_for_circuit_name_edit = QLineEdit(self.home_page_to_add_tour)
        self.input_for_circuit_name_edit.setObjectName(u"input_for_circuit_name_edit")
        self.input_for_circuit_name_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.input_for_circuit_name_edit, 0, 1, 1, 1)

        self.label_6 = QLabel(self.home_page_to_add_tour)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.input_for_travel_description = QPlainTextEdit(self.home_page_to_add_tour)
        self.input_for_travel_description.setObjectName(u"input_for_travel_description")
        self.input_for_travel_description.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.input_for_travel_description, 5, 0, 1, 7)

        self.label_8 = QLabel(self.home_page_to_add_tour)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 11))

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.input_for_difficulty_of_travel = QLineEdit(self.home_page_to_add_tour)
        self.input_for_difficulty_of_travel.setObjectName(u"input_for_difficulty_of_travel")
        self.input_for_difficulty_of_travel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.input_for_difficulty_of_travel, 0, 6, 1, 1)

        self.btn_to_go_page_2_for_adding_tour = QPushButton(self.home_page_to_add_tour)
        self.btn_to_go_page_2_for_adding_tour.setObjectName(u"btn_to_go_page_2_for_adding_tour")
        self.btn_to_go_page_2_for_adding_tour.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.gridLayout.addWidget(self.btn_to_go_page_2_for_adding_tour, 6, 6, 1, 1)

        self.imported_file_label = QLabel(self.home_page_to_add_tour)
        self.imported_file_label.setObjectName(u"imported_file_label")

        self.gridLayout.addWidget(self.imported_file_label, 3, 4, 1, 3)

        self.button_to_cancel_new_add = QPushButton(self.home_page_to_add_tour)
        self.button_to_cancel_new_add.setObjectName(u"button_to_cancel_new_add")
        self.button_to_cancel_new_add.setStyleSheet(u"background-color: rgb(224, 27, 36);")

        self.gridLayout.addWidget(self.button_to_cancel_new_add, 6, 5, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.home_page_to_add_tour)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: rgb(38, 162, 105);\n"
"")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_9)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table_view_to_list_existing_tool_for_travel = QTableView(self.page_2)
        self.table_view_to_list_existing_tool_for_travel.setObjectName(u"table_view_to_list_existing_tool_for_travel")

        self.gridLayout_2.addWidget(self.table_view_to_list_existing_tool_for_travel, 2, 0, 1, 1)

        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.input_for_new_tool_for_travel = QLineEdit(self.page_2)
        self.input_for_new_tool_for_travel.setObjectName(u"input_for_new_tool_for_travel")
        self.input_for_new_tool_for_travel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.input_for_new_tool_for_travel, 1, 1, 1, 1)

        self.btn_for_new_tool_validation = QPushButton(self.page_2)
        self.btn_for_new_tool_validation.setObjectName(u"btn_for_new_tool_validation")

        self.gridLayout_2.addWidget(self.btn_for_new_tool_validation, 1, 2, 1, 1)

        self.table_view_to_list_new_tool_for_new_travel = QTableView(self.page_2)
        self.table_view_to_list_new_tool_for_new_travel.setObjectName(u"table_view_to_list_new_tool_for_new_travel")

        self.gridLayout_2.addWidget(self.table_view_to_list_new_tool_for_new_travel, 2, 1, 1, 2)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_back_to_page1 = QPushButton(self.page_2)
        self.btn_back_to_page1.setObjectName(u"btn_back_to_page1")
        self.btn_back_to_page1.setStyleSheet(u"background-color: rgb(237, 51, 59);")

        self.horizontalLayout.addWidget(self.btn_back_to_page1)

        self.btn_to_slide_to_page3 = QPushButton(self.page_2)
        self.btn_to_slide_to_page3.setObjectName(u"btn_to_slide_to_page3")
        self.btn_to_slide_to_page3.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout.addWidget(self.btn_to_slide_to_page3)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_11)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.input_for_new_adrenaline = QLineEdit(self.page_3)
        self.input_for_new_adrenaline.setObjectName(u"input_for_new_adrenaline")
        self.input_for_new_adrenaline.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.input_for_new_adrenaline, 0, 1, 1, 1)

        self.label_12 = QLabel(self.page_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)

        self.input_for_new_adrenaline_validation = QPushButton(self.page_3)
        self.input_for_new_adrenaline_validation.setObjectName(u"input_for_new_adrenaline_validation")

        self.gridLayout_3.addWidget(self.input_for_new_adrenaline_validation, 0, 2, 1, 1)

        self.tableview_for_all_available_adrenaline = QTableView(self.page_3)
        self.tableview_for_all_available_adrenaline.setObjectName(u"tableview_for_all_available_adrenaline")

        self.gridLayout_3.addWidget(self.tableview_for_all_available_adrenaline, 1, 0, 1, 1)

        self.table_view_for_all_adrenaline_for_neww_travel = QTableView(self.page_3)
        self.table_view_for_all_adrenaline_for_neww_travel.setObjectName(u"table_view_for_all_adrenaline_for_neww_travel")

        self.gridLayout_3.addWidget(self.table_view_for_all_adrenaline_for_neww_travel, 1, 1, 1, 2)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.input_for_back_to_page2 = QPushButton(self.page_3)
        self.input_for_back_to_page2.setObjectName(u"input_for_back_to_page2")
        self.input_for_back_to_page2.setStyleSheet(u"background-color: rgb(237, 51, 59);")

        self.horizontalLayout_3.addWidget(self.input_for_back_to_page2)

        self.btn_to_go_to_the_page_3 = QPushButton(self.page_3)
        self.btn_to_go_to_the_page_3.setObjectName(u"btn_to_go_to_the_page_3")
        self.btn_to_go_to_the_page_3.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_3.addWidget(self.btn_to_go_to_the_page_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_5 = QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_13 = QLabel(self.page_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_13)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_to_validate_new_task_added_for_travel = QPushButton(self.page_4)
        self.btn_to_validate_new_task_added_for_travel.setObjectName(u"btn_to_validate_new_task_added_for_travel")

        self.gridLayout_4.addWidget(self.btn_to_validate_new_task_added_for_travel, 0, 2, 1, 1)

        self.label_14 = QLabel(self.page_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)

        self.input_to_add_new_task_included_in_price = QLineEdit(self.page_4)
        self.input_to_add_new_task_included_in_price.setObjectName(u"input_to_add_new_task_included_in_price")
        self.input_to_add_new_task_included_in_price.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.input_to_add_new_task_included_in_price, 0, 1, 1, 1)

        self.table_view_for_all_task_already_available_recently = QTableView(self.page_4)
        self.table_view_for_all_task_already_available_recently.setObjectName(u"table_view_for_all_task_already_available_recently")

        self.gridLayout_4.addWidget(self.table_view_for_all_task_already_available_recently, 1, 0, 1, 1)

        self.table_view_to_list_all_new_included_task_for_new_tour = QTableView(self.page_4)
        self.table_view_to_list_all_new_included_task_for_new_tour.setObjectName(u"table_view_to_list_all_new_included_task_for_new_tour")

        self.gridLayout_4.addWidget(self.table_view_to_list_all_new_included_task_for_new_tour, 1, 1, 1, 2)


        self.verticalLayout_5.addLayout(self.gridLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.btn_back_to_the_page3 = QPushButton(self.page_4)
        self.btn_back_to_the_page3.setObjectName(u"btn_back_to_the_page3")
        self.btn_back_to_the_page3.setStyleSheet(u"background-color: rgb(224, 27, 36);")

        self.horizontalLayout_4.addWidget(self.btn_back_to_the_page3)

        self.btn_to_go_to_the_last_page_for_verification_into_page5 = QPushButton(self.page_4)
        self.btn_to_go_to_the_last_page_for_verification_into_page5.setObjectName(u"btn_to_go_to_the_last_page_for_verification_into_page5")
        self.btn_to_go_to_the_last_page_for_verification_into_page5.setStyleSheet(u"background-color: rgb(38, 162, 105);\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_to_go_to_the_last_page_for_verification_into_page5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_6 = QVBoxLayout(self.page_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_15 = QLabel(self.page_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_15)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_for_tour_name_to_generate_from_python = QLabel(self.page_5)
        self.label_for_tour_name_to_generate_from_python.setObjectName(u"label_for_tour_name_to_generate_from_python")
        self.label_for_tour_name_to_generate_from_python.setMinimumSize(QSize(200, 0))
        self.label_for_tour_name_to_generate_from_python.setMaximumSize(QSize(200, 16777215))
        self.label_for_tour_name_to_generate_from_python.setFont(font)
        self.label_for_tour_name_to_generate_from_python.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_for_tour_name_to_generate_from_python)

        self.label_for_subtitle_to_generate_from_python = QLabel(self.page_5)
        self.label_for_subtitle_to_generate_from_python.setObjectName(u"label_for_subtitle_to_generate_from_python")
        self.label_for_subtitle_to_generate_from_python.setFont(font)
        self.label_for_subtitle_to_generate_from_python.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_for_subtitle_to_generate_from_python)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.label_17 = QLabel(self.page_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_17)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_for_travel_duration = QLabel(self.page_5)
        self.label_for_travel_duration.setObjectName(u"label_for_travel_duration")
        self.label_for_travel_duration.setFont(font)
        self.label_for_travel_duration.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_for_travel_duration, 0, 1, 1, 1)

        self.label_for_travel_pricing = QLabel(self.page_5)
        self.label_for_travel_pricing.setObjectName(u"label_for_travel_pricing")
        self.label_for_travel_pricing.setFont(font)
        self.label_for_travel_pricing.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_for_travel_pricing, 0, 0, 1, 1)

        self.label_for_difficulty = QLabel(self.page_5)
        self.label_for_difficulty.setObjectName(u"label_for_difficulty")
        self.label_for_difficulty.setFont(font)
        self.label_for_difficulty.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_for_difficulty, 0, 2, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_5)

        self.label_16 = QLabel(self.page_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_16)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.table_view_to_list_all_adrenaline_before_validation = QTableView(self.page_5)
        self.table_view_to_list_all_adrenaline_before_validation.setObjectName(u"table_view_to_list_all_adrenaline_before_validation")

        self.gridLayout_6.addWidget(self.table_view_to_list_all_adrenaline_before_validation, 1, 1, 1, 1)

        self.table_view_to_list_all_included_in_price_before_validation = QTableView(self.page_5)
        self.table_view_to_list_all_included_in_price_before_validation.setObjectName(u"table_view_to_list_all_included_in_price_before_validation")

        self.gridLayout_6.addWidget(self.table_view_to_list_all_included_in_price_before_validation, 1, 2, 1, 1)

        self.table_view_to_list_all_tool_before_validation = QTableView(self.page_5)
        self.table_view_to_list_all_tool_before_validation.setObjectName(u"table_view_to_list_all_tool_before_validation")

        self.gridLayout_6.addWidget(self.table_view_to_list_all_tool_before_validation, 1, 0, 1, 1)

        self.label_20 = QLabel(self.page_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_20, 0, 2, 1, 1)

        self.label_19 = QLabel(self.page_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_19, 0, 1, 1, 1)

        self.label_18 = QLabel(self.page_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.btn_to_back_into_page_4 = QPushButton(self.page_5)
        self.btn_to_back_into_page_4.setObjectName(u"btn_to_back_into_page_4")
        self.btn_to_back_into_page_4.setStyleSheet(u"background-color: rgb(224, 27, 36);")

        self.horizontalLayout_6.addWidget(self.btn_to_back_into_page_4)

        self.btn_validation_for_tour = QPushButton(self.page_5)
        self.btn_validation_for_tour.setObjectName(u"btn_validation_for_tour")
        self.btn_validation_for_tour.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_6.addWidget(self.btn_validation_for_tour)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Magadagascar_Tours)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Magadagascar_Tours)
    # setupUi

    def retranslateUi(self, Magadagascar_Tours):
        Magadagascar_Tours.setWindowTitle(QCoreApplication.translate("Magadagascar_Tours", u"Madagascar-Tours", None))
        self.label.setText(QCoreApplication.translate("Magadagascar_Tours", u"Ajout de nouveau circuit", None))
        self.input_for_night_number_for_travel.setPlaceholderText(QCoreApplication.translate("Magadagascar_Tours", u"Nuit", None))
        self.label_7.setText(QCoreApplication.translate("Magadagascar_Tours", u"Images", None))
        self.input_for_day_number_for_travel.setPlaceholderText(QCoreApplication.translate("Magadagascar_Tours", u"Jours", None))
        self.Btn_for_choosing_file.setText(QCoreApplication.translate("Magadagascar_Tours", u"importer une image", None))
        self.input_for_price_of_travel.setPlaceholderText(QCoreApplication.translate("Magadagascar_Tours", u"5000", None))
        self.label_5.setText(QCoreApplication.translate("Magadagascar_Tours", u"Sous-titre", None))
        self.label_3.setText(QCoreApplication.translate("Magadagascar_Tours", u"Dur\u00e9e du voyage", None))
        self.label_4.setText(QCoreApplication.translate("Magadagascar_Tours", u"Difficult\u00e9", None))
        self.input_for_little_description_of_travel.setPlaceholderText(QCoreApplication.translate("Magadagascar_Tours", u"Un petit sous-titre du trajet", None))
        self.label_2.setText(QCoreApplication.translate("Magadagascar_Tours", u"Nom du circuit", None))
        self.label_6.setText(QCoreApplication.translate("Magadagascar_Tours", u"Prix", None))
        self.label_8.setText(QCoreApplication.translate("Magadagascar_Tours", u"D\u00e9scription", None))
        self.input_for_difficulty_of_travel.setPlaceholderText(QCoreApplication.translate("Magadagascar_Tours", u"100", None))
        self.btn_to_go_page_2_for_adding_tour.setText(QCoreApplication.translate("Magadagascar_Tours", u"Suivant", None))
        self.imported_file_label.setText(QCoreApplication.translate("Magadagascar_Tours", u"Aucun fichier trouv\u00e9", None))
        self.button_to_cancel_new_add.setText(QCoreApplication.translate("Magadagascar_Tours", u"Annuler", None))
        self.label_9.setText(QCoreApplication.translate("Magadagascar_Tours", u"Equipement requis lors du trajet", None))
        self.label_10.setText(QCoreApplication.translate("Magadagascar_Tours", u"Ajouter un nouvel \u00e9quipement", None))
        self.input_for_new_tool_for_travel.setPlaceholderText(QCoreApplication.translate("Magadagascar_Tours", u"Une Hache", None))
        self.btn_for_new_tool_validation.setText(QCoreApplication.translate("Magadagascar_Tours", u"OK", None))
        self.btn_back_to_page1.setText(QCoreApplication.translate("Magadagascar_Tours", u"Revenir \u00e0 la page pr\u00e9c\u00e9dente", None))
        self.btn_to_slide_to_page3.setText(QCoreApplication.translate("Magadagascar_Tours", u"Passer \u00e0 l'\u00e9tape suivante", None))
        self.label_11.setText(QCoreApplication.translate("Magadagascar_Tours", u"Les points fort du trajet", None))
        self.input_for_new_adrenaline.setPlaceholderText(QCoreApplication.translate("Magadagascar_Tours", u"La mort", None))
        self.label_12.setText(QCoreApplication.translate("Magadagascar_Tours", u"Ajout d'un nouveau", None))
        self.input_for_new_adrenaline_validation.setText(QCoreApplication.translate("Magadagascar_Tours", u"OK", None))
        self.input_for_back_to_page2.setText(QCoreApplication.translate("Magadagascar_Tours", u"Revenir \u00e0 la page pr\u00e9c\u00e9dente", None))
        self.btn_to_go_to_the_page_3.setText(QCoreApplication.translate("Magadagascar_Tours", u"Passer \u00e0 l'\u00e9tape suivante", None))
        self.label_13.setText(QCoreApplication.translate("Magadagascar_Tours", u"Les taches incluse dans le prix", None))
        self.btn_to_validate_new_task_added_for_travel.setText(QCoreApplication.translate("Magadagascar_Tours", u"OK", None))
        self.label_14.setText(QCoreApplication.translate("Magadagascar_Tours", u"Ajout de nouvelle tache", None))
        self.input_to_add_new_task_included_in_price.setPlaceholderText(QCoreApplication.translate("Magadagascar_Tours", u"La bouff", None))
        self.btn_back_to_the_page3.setText(QCoreApplication.translate("Magadagascar_Tours", u"Revenit a la page pr\u00e9c\u00e9dentes", None))
        self.btn_to_go_to_the_last_page_for_verification_into_page5.setText(QCoreApplication.translate("Magadagascar_Tours", u"Verifier toutes les informations", None))
        self.label_15.setText(QCoreApplication.translate("Magadagascar_Tours", u"Pr\u00e9sentation du circuit", None))
        self.label_for_tour_name_to_generate_from_python.setText(QCoreApplication.translate("Magadagascar_Tours", u"Tsimbazaza", None))
        self.label_for_subtitle_to_generate_from_python.setText(QCoreApplication.translate("Magadagascar_Tours", u"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical ,....", None))
        self.label_17.setText(QCoreApplication.translate("Magadagascar_Tours", u"D\u00e9tails techniques", None))
        self.label_for_travel_duration.setText(QCoreApplication.translate("Magadagascar_Tours", u"5 jours / 5 Nuits", None))
        self.label_for_travel_pricing.setText(QCoreApplication.translate("Magadagascar_Tours", u"5000 E", None))
        self.label_for_difficulty.setText(QCoreApplication.translate("Magadagascar_Tours", u"100%", None))
        self.label_16.setText(QCoreApplication.translate("Magadagascar_Tours", u"Autres informations", None))
        self.label_20.setText(QCoreApplication.translate("Magadagascar_Tours", u"Les taches incluses dans le prix", None))
        self.label_19.setText(QCoreApplication.translate("Magadagascar_Tours", u"Moments forts du trajets", None))
        self.label_18.setText(QCoreApplication.translate("Magadagascar_Tours", u"Equipements n\u00e9cessaires", None))
        self.btn_to_back_into_page_4.setText(QCoreApplication.translate("Magadagascar_Tours", u"Revenir sur la page pr\u00e9c\u00e9dente", None))
        self.btn_validation_for_tour.setText(QCoreApplication.translate("Magadagascar_Tours", u"Valider l'enregistrement", None))
    # retranslateUi

