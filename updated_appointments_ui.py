# Form implementation generated from reading ui file 'c:\Users\hp\Documents\GitHub\db_project\updated_appointments.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 450)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.apptable = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.apptable.setEnabled(True)
        self.apptable.setGeometry(QtCore.QRect(30, 140, 611, 231))
        self.apptable.setObjectName("apptable")
        self.apptable.setColumnCount(5)
        self.apptable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.apptable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.apptable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.apptable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.apptable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.apptable.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.view_app_details = QtWidgets.QPushButton(parent=self.centralwidget)
        self.view_app_details.setGeometry(QtCore.QRect(520, 380, 91, 21))
        self.view_app_details.setObjectName("view_app_details")
        self.search_app = QtWidgets.QPushButton(parent=self.centralwidget)
        self.search_app.setGeometry(QtCore.QRect(550, 40, 81, 21))
        self.search_app.setObjectName("search_app")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 81, 16))
        self.label_2.setObjectName("label_2")
        self.patient_app = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.patient_app.setGeometry(QtCore.QRect(120, 40, 391, 20))
        self.patient_app.setObjectName("patient_app")
        self.back_to_doc_home = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_to_doc_home.setGeometry(QtCore.QRect(60, 380, 91, 21))
        self.back_to_doc_home.setObjectName("back_to_doc_home")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 90, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 81, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 90, 41, 31))
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(390, 90, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 90, 71, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 80, 51, 31))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 18))
        self.menubar.setObjectName("menubar")
        self.menupayment_details = QtWidgets.QMenu(parent=self.menubar)
        self.menupayment_details.setObjectName("menupayment_details")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menupayment_details.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.apptable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Patient Name"))
        item = self.apptable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Doctor Name"))
        item = self.apptable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Appointment Time"))
        item = self.apptable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Day"))
        item = self.apptable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cancelled"))
        self.label.setText(_translate("MainWindow", "Appointments Booked"))
        self.view_app_details.setText(_translate("MainWindow", "View"))
        self.search_app.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "Patient Name:"))
        self.back_to_doc_home.setText(_translate("MainWindow", "Back"))
        self.label_3.setText(_translate("MainWindow", "Filter"))
        self.label_4.setText(_translate("MainWindow", "day:"))
        self.label_6.setText(_translate("MainWindow", "By Doctor:"))
        self.label_7.setText(_translate("MainWindow", "Filter by"))
        self.menupayment_details.setTitle(_translate("MainWindow", "appointments"))
