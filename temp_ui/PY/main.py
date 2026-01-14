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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableView,
    QVBoxLayout, QWidget)

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
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(38, 162, 105);\n"
"")

        self.verticalLayout_5.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.database_name = QLineEdit(self.page_2)
        self.database_name.setObjectName(u"database_name")
        self.database_name.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.database_name, 2, 1, 1, 1)

        self.database_hosting = QLineEdit(self.page_2)
        self.database_hosting.setObjectName(u"database_hosting")
        self.database_hosting.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.database_hosting, 1, 1, 1, 1)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.page_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit, 5, 1, 1, 1)

        self.user_name = QLineEdit(self.page_2)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.user_name, 3, 1, 1, 1)

        self.database_password = QLineEdit(self.page_2)
        self.database_password.setObjectName(u"database_password")
        self.database_password.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.database_password, 4, 1, 1, 1)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_8 = QLabel(self.page_2)
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

        self.btn_save_data_information = QPushButton(self.page_2)
        self.btn_save_data_information.setObjectName(u"btn_save_data_information")
        font1 = QFont()
        font1.setBold(False)
        self.btn_save_data_information.setFont(font1)
        self.btn_save_data_information.setStyleSheet(u"background-color: rgb(38, 162, 105);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.btn_save_data_information)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_2)
        self.circuits_ui = QWidget()
        self.circuits_ui.setObjectName(u"circuits_ui")
        self.verticalLayout_2 = QVBoxLayout(self.circuits_ui)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.circuits_ui)
        self.label.setObjectName(u"label")
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
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.table_to_list_contact = QTableView(self.page)
        self.table_to_list_contact.setObjectName(u"table_to_list_contact")

        self.verticalLayout_4.addWidget(self.table_to_list_contact)

        self.stackedWidget.addWidget(self.page)

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

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Madagascar-Tours", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Mots de passe pour la base de donn\u00e9es", None))
        self.database_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"local_caponmada", None))
        self.database_hosting.setPlaceholderText(QCoreApplication.translate("MainWindow", u"caponmada.mg/192.168.1.1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nom de base de donn\u00e9es", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"3306", None))
        self.user_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"root", None))
        self.database_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"root", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Adresse de la base de donn\u00e9es", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Numero de port", None))
        self.btn_save_data_information.setText(QCoreApplication.translate("MainWindow", u"Enregistrer les modifications", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Circuits", None))
        self.btn_add_new_tour.setText(QCoreApplication.translate("MainWindow", u"Ajouter de nouveau circuit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.tours_btn.setText(QCoreApplication.translate("MainWindow", u"Circuits", None))
        self.contact_btn.setText(QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.config_btn.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
    # retranslateUi

