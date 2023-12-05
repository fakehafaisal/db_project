from PyQt6 import QtWidgets, uic, QtGui, QtCore
from PyQt6.QtWidgets import QDialog, QApplication, QWidget,  QGridLayout, QListWidget,  QPushButton, QMainWindow, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QRadioButton, QHBoxLayout, QHeaderView
import sys 
from datetime import date
import pyodbc
from PyQt6.QtCore import Qt


server = 'DESKTOP-HPUUN98\SPARTA'
database = 'db_project'  # Name of your Northwind database
use_windows_authentication = True  # Set to True to use Windows Authentication

# 1main homepage
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("Homepage.ui", self)
        self.setWindowTitle("Welcome Page")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()

        self.Next.clicked.connect(self.click_next) 

        self.Cancel.clicked.connect(self.Cancel_app)
        

    def click_next(self):
        self.new_form = ViewBook3()
        self.new_form.show()
        self.close()

    def Cancel_app(self):
        self.close()

# 2signup page 
class ViewBook(QtWidgets.QMainWindow):  
    def __init__(self):
        super(ViewBook, self).__init__() 
        uic.loadUi('signuppage.ui', self) 
        self.setWindowTitle("SignUp Page")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()

        self.Next2.clicked.connect(self.click_next2) 

        self.login_button.clicked.connect(self.Login_page)

    def Login_page(self):
        self.new_form = ViewBook3()
        self.new_form.show()
        self.close()

    def click_next2(self):
            first_name = self.FirstName.text()  
            last_name = self.LastName.text() 
            email = self.email.text() 
            password = self.password.text()  
            confirm_password = self.confirmpassword.text()

            if (self.patientselect.isChecked() == False) and (self.doctorselect.isChecked()==False):
                output=QMessageBox(self)              
                output.setWindowTitle("Unidentified Person") 
                output.setText("Please choose sign up as Patient or Doctor.")
                output.setStandardButtons( QMessageBox.StandardButton.Ok)
                output.setIcon(QMessageBox.Icon.Warning) 
                button=output.exec()

            elif ((len(first_name)==0) or (len(last_name)==0)):
                output=QMessageBox(self)              
                output.setWindowTitle("No Name") 
                output.setText("Please enter Name.")
                output.setStandardButtons( QMessageBox.StandardButton.Ok)
                output.setIcon(QMessageBox.Icon.Warning) 
                button=output.exec()

            elif (first_name.isalpha() == False):
                output=QMessageBox(self)              
                output.setWindowTitle("Wrong Name Entry") 
                output.setText("First Name should only consist of letters")
                output.setStandardButtons( QMessageBox.StandardButton.Ok)
                output.setIcon(QMessageBox.Icon.Warning) 
                button=output.exec()

            elif (last_name.isalpha() == False):
                output=QMessageBox(self)              
                output.setWindowTitle("Wrong Name Entry") 
                output.setText("Last Name should only consist of letters")
                output.setStandardButtons( QMessageBox.StandardButton.Ok)
                output.setIcon(QMessageBox.Icon.Warning) 
                button=output.exec()    

            elif (len(email)==0):
                output=QMessageBox(self)              
                output.setWindowTitle("No Email Entry") 
                output.setText("Please Enter Email")
                output.setStandardButtons( QMessageBox.StandardButton.Ok)
                output.setIcon(QMessageBox.Icon.Warning) 
                button=output.exec() 

            elif ((len(password)<=7 and len(password)>=0) or (password.isalpha() == True)):
                output=QMessageBox(self)              
                output.setWindowTitle("Weak Password") 
                output.setText("Please use a strong password.")
                output.setStandardButtons( QMessageBox.StandardButton.Ok)
                output.setIcon(QMessageBox.Icon.Warning) 
                button=output.exec()
            
            elif ((len(password)==0)):
                output=QMessageBox(self)              
                output.setWindowTitle("No Password") 
                output.setText("Please enter password.")
                output.setStandardButtons( QMessageBox.StandardButton.Ok)
                output.setIcon(QMessageBox.Icon.Warning) 
                button=output.exec()

            elif (password != confirm_password):
                output=QMessageBox(self)              
                output.setWindowTitle("Wrong Entry") 
                output.setText("Password should be same as Confirm Password.")
                output.setStandardButtons( QMessageBox.StandardButton.Ok)
                output.setIcon(QMessageBox.Icon.Warning) 
                button=output.exec()

            else:
                if (self.patientselect.isChecked()==True):
                    self.new_form = ViewBook2(first_name, last_name, email, password, confirm_password)
                    self.new_form.show()
                    self.close()
                elif (self.doctorselect.isChecked()==True):
                    self.new_form = ViewBook4(first_name, last_name, email, password, confirm_password)
                    self.new_form.show()
                    self.close()
 
# 3signup page 2
class ViewBook2(QtWidgets.QMainWindow):  
    def __init__(self, first_name, last_name, email, password, confirm_password):
        super(ViewBook2, self).__init__() 
        uic.loadUi('signuppage2.ui', self) 
        self.setWindowTitle("Patient Signup")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.patient_select.setChecked(True)
        self.lineEdit.setText(first_name)
        self.lineEdit_6.setText(last_name)
        self.lineEdit_4.setText(email)
        self.lineEdit_3.setText(password)
        self.lineEdit_2.setText(confirm_password)
        self.show()

        self.Next3.clicked.connect(self.signup_done) 

        self.Cancel3.clicked.connect(self.final_cancel)

    def signup_done(self):
        DOB=self.DOB.date() 
        phone_num = self.phonenumber.text()
        current_date = date.today()

        if (DOB >= current_date):
            output=QMessageBox(self)              
            output.setWindowTitle("Incorrect DOB") 
            output.setText("Please enter correct Date of Birth.")
            output.setStandardButtons( QMessageBox.StandardButton.Ok)
            output.setIcon(QMessageBox.Icon.Warning) 
            button=output.exec()

        elif (len(phone_num)==0):
            output=QMessageBox(self)              
            output.setWindowTitle("No Phone Number") 
            output.setText("Please enter Phone Number.") 
            output.setStandardButtons( QMessageBox.StandardButton.Ok)
            output.setIcon(QMessageBox.Icon.Warning) 
            button=output.exec()

        elif ((phone_num.isnumeric() == False) or (len(phone_num) != 11)):
            output=QMessageBox(self)              
            output.setWindowTitle("Incorrect Phone Number") 
            output.setText("Please enter correct Phone Number.") 
            output.setStandardButtons( QMessageBox.StandardButton.Ok)
            output.setIcon(QMessageBox.Icon.Warning) 
            button=output.exec()
        
        elif ((phone_num.isnumeric() == True) and (DOB < current_date)):
            self.insert_patient_details()
            output=QMessageBox(self)              
            output.setWindowTitle("Sign Up Complete") 
            output.setText("Sign Up Completed Successfully!")
            output.setStandardButtons( QMessageBox.StandardButton.Ok)
            output.setIcon(QMessageBox.Icon.Information) 
            button=output.exec()
            self.new_form = ViewBook3()
            self.new_form.show()
            self.close()

    def final_cancel(self):
        self.close()
    
    def insert_patient_details(self):
        # print("Function called")
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        sql_query = """
            INSERT INTO patients
            ([patient_id],[first_name],[last_name],[email],[password],[confirm_password],[DOB],[gender_id],[contact],[emergency_contact], [patient_weight])
            VALUES (?,?,?,?,?,?,?,?,?,?,?)
        """
        cursor.execute("SELECT max(patient_id) AS patient_id from patients")
        result = cursor.fetchone()
        patient_id = result[0] + 1
        
        first_name = self.lineEdit.text()
        last_name = self.lineEdit_6.text()
        email = self.lineEdit_4.text()
        password = self.lineEdit_3.text()
        confirm_password = self.lineEdit_2.text()
        DOB = self.DOB.date().toString("yyyy-MM-dd")

        if self.comboBox.currentText()=="Male":
            gender_id = 1
        elif self.comboBox.currentText()=="Female":
            gender_id = 2
        elif self.comboBox.currentText()=="Other":
            gender_id = 3
    
        contact = self.phonenumber.text()
        emergency_contact = self.phonenumber_2.text()
        patient_weight = 70


        # Execute the SQL query with parameter values

        cursor.execute(sql_query, (int(patient_id),first_name,last_name, email, password, confirm_password, DOB, int(gender_id), contact,emergency_contact,patient_weight))
        connection.commit()
        connection.close()

# 4login screen
class ViewBook3(QtWidgets.QMainWindow):  
    def __init__(self):
        super(ViewBook3, self).__init__() 
        uic.loadUi('LOGINTHERAHOPE.ui', self) 
        self.setWindowTitle("Login Page")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()

        self.pushButton_2.clicked.connect(self.Login_clicked) 

        self.pushButton.clicked.connect(self.cancel) 

        self.signup.clicked.connect(self.sign_up_page)

    def Login_clicked(self):
        login_email = self.lineEdit_2.text()  
        login_password = self.lineEdit_3.text()  

        if ((self.radioButton.isChecked() == False) and (self.radioButton_2.isChecked() == False) and (self.radioButton_3.isChecked() == False)):
            output=QMessageBox(self)              
            output.setWindowTitle("Unidentified Person") 
            output.setText("Please Choose from Admin, Doctor or Patient.")
            output.setStandardButtons( QMessageBox.StandardButton.Ok)
            output.setIcon(QMessageBox.Icon.Warning) 
            button=output.exec()

        elif (len(login_email)==0):
            output=QMessageBox(self)              
            output.setWindowTitle("No Email") 
            output.setText("Please Enter Email.")
            output.setStandardButtons( QMessageBox.StandardButton.Ok)
            output.setIcon(QMessageBox.Icon.Warning) 
            button=output.exec()

        elif (len(login_password)==0):
            output=QMessageBox(self)              
            output.setWindowTitle("No password") 
            output.setText("Please Enter Password.")
            output.setStandardButtons( QMessageBox.StandardButton.Ok)
            output.setIcon(QMessageBox.Icon.Warning) 
            button=output.exec()

        elif ((len(login_password)<=5 and len(login_password)>0) or (login_password.isalpha() == True)):
                output=QMessageBox(self)              
                output.setWindowTitle("Weak Password") 
                output.setText("Please use a strong password.")
                output.setStandardButtons( QMessageBox.StandardButton.Ok)
                output.setIcon(QMessageBox.Icon.Warning) 
                button=output.exec()

        else:
            if (self.radioButton.isChecked()==True):
                if self.verifyDoctorCredentials(login_email, login_password):
                    self.new_form = Doctor_homepage("doctor")
                    self.new_form.show()
                    self.close()
                else:
                    output=QMessageBox(self)              
                    output.setWindowTitle("Error") 
                    output.setText("Invalid Doctor credentials")
                    output.setStandardButtons( QMessageBox.StandardButton.Ok)
                    output.setIcon(QMessageBox.Icon.Warning) 
                    button = output.exec() 

            elif (self.radioButton_2.isChecked()==True):
                if self.verifyPatientCredentials(login_email, login_password):
                    self.new_form = Patient_homepage(login_email)
                    self.new_form.show()
                    self.close()
                else:
                    output=QMessageBox(self)              
                    output.setWindowTitle("Error") 
                    output.setText("Invalid Patient credentials")
                    output.setStandardButtons( QMessageBox.StandardButton.Ok)
                    output.setIcon(QMessageBox.Icon.Warning) 
                    button = output.exec() 

            elif (self.radioButton_3.isChecked()==True):
                if self.verifyAdminCredentials(login_email, login_password):
                    self.new_form = Admin_homepage("admin") 
                    self.new_form.show()
                    self.close()
                else:
                    output=QMessageBox(self)              
                    output.setWindowTitle("Error") 
                    output.setText("Invalid Admin credentials")
                    output.setStandardButtons( QMessageBox.StandardButton.Ok)
                    output.setIcon(QMessageBox.Icon.Warning) 
                    button = output.exec() 
    
    def cancel(self):
        self.close()

    def sign_up_page(self):
        self.new_form = ViewBook()
        self.new_form.show()
        self.close()

    def verifyDoctorCredentials(self, login_email, login_password):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM [doctor]
            WHERE email = ? AND password = ?
        """, (login_email, login_password))

        return cursor.fetchone() is not None
    
    def verifyPatientCredentials(self, login_email, login_password):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM [patients]
            WHERE email = ? AND password = ?
        """, (login_email, login_password))

        return cursor.fetchone() is not None

    def verifyAdminCredentials(self, login_email, login_password):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM [admin_employee]
            WHERE email = ? AND password = ?
        """, (login_email, login_password))

        return cursor.fetchone() is not None


# 5doctor signup
class ViewBook4(QtWidgets.QMainWindow):  
    def __init__(self, first_name, last_name, email, password, confirm_password):
        super(ViewBook4, self).__init__() 
        uic.loadUi('doctorsignup.ui', self) 
        self.setWindowTitle("Doctor SignUp Page")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.doctor_select.setChecked(True)
        self.doc_fname.setText(first_name)
        self.doc_last_name.setText(last_name)
        self.doc_email.setText(email)
        self.doc_password.setText(password)
        self.doc_confirm.setText(confirm_password)

        self.show()

        self.doc_done.clicked.connect(self.doc_signup_done)

        self.Cancel_doc_signup.clicked.connect(self.doc_cancel)

    def doc_signup_done(self):
        gender = self.Gender.currentText()
        cnic = self.CNIC.text()
        license = self.medical_license.text()

        if len(cnic)==0:
            output=QMessageBox(self)              
            output.setWindowTitle("No CNIC entered.") 
            output.setText("Please enter CNIC number.")
            output.setStandardButtons( QMessageBox.StandardButton.Ok)
            output.setIcon(QMessageBox.Icon.Warning) 
            button=output.exec()

        elif len(license)==0:
            output=QMessageBox(self)              
            output.setWindowTitle("No Medical License entered.") 
            output.setText("Please enter Medical License number.")
            output.setStandardButtons( QMessageBox.StandardButton.Ok)
            output.setIcon(QMessageBox.Icon.Warning) 
            button=output.exec()

        else:
            self.insert_doc_details()
            output=QMessageBox(self)              
            output.setWindowTitle("Sign up Sucessful.") 
            output.setText("Account awaiting Admin Approval.")
            output.setStandardButtons( QMessageBox.StandardButton.Ok)
            output.setIcon(QMessageBox.Icon.Information) 
            button=output.exec()
            # self.new_form = ViewBook3()
            # self.new_form.show()
            # self.close()


    def doc_cancel(self):
        self.close()

    def insert_doc_details(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        sql_query = """
            INSERT INTO doctor
            ([doctor_id],[first_name],[last_name],[email],[password],[confirm_password],[gender_id],[CNIC],[medical_license_num])
            VALUES (?,?,?,?,?,?,?,?,?)
        """

        cursor.execute("SELECT max(doctor_id) AS doctor_id from doctor")
        result = cursor.fetchone()
        doctor_id = result[0] + 1

        first_name = self.doc_fname.text()
        last_name = self.doc_last_name.text()
        email = self.doc_email.text()
        password = self.doc_password.text()
        confirm_password = self.doc_confirm.text()

        if self.Gender.currentText()=="Male":
            gender_id = 1
        elif self.Gender.currentText()=="Female":
            gender_id = 2

        CNIC = self.CNIC.text()
        medical_license_num = self.medical_license.text()

        cursor.execute(sql_query, (int(doctor_id),first_name,last_name, email, password, confirm_password, int(gender_id), CNIC,medical_license_num))
        connection.commit()
        connection.close()
# 6admin homepage
class Admin_homepage(QtWidgets.QMainWindow):  
    def __init__(self,user):
        super(Admin_homepage, self).__init__() 
        uic.loadUi('adminhomepage.ui', self) 
        self.setWindowTitle("Admin Homepage")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        print(user)
        self.show()

        self.logout_admin.clicked.connect(self.admin_logout)

        self.patient_admin.clicked.connect(self.admin_patient_view)

        self.doc_admin.clicked.connect(self.admin_doc_view)
    
        self.payments.clicked.connect(self.view_payments)

        self.doc_approval.clicked.connect(self.approvals_disapproval)


    def admin_logout(self):
        self.new_form = ViewBook3()
        self.new_form.show()
        self.close()

    def admin_doc_view(self):
        self.new_form = doctors_list()
        self.new_form.show()
        self.close()

    def admin_patient_view(self):
        self.new_form = Patient_Records("admin")
        self.new_form.show()
        self.close()

    def view_payments(self):
        self.new_form = payment_details()
        self.new_form.show()
        self.close()

    def approvals_disapproval(self):
        self.new_form = MedicalApprovalScreen()
        self.new_form.show()
        self.close()

# 7doctor homepage
class Doctor_homepage(QtWidgets.QMainWindow):  
    def __init__(self,user):
        super(Doctor_homepage, self).__init__() 
        uic.loadUi('dochomepage.ui', self) 
        self.setWindowTitle("Doctor Homepage")
        
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()

        self.logout_doctor.clicked.connect(self.patient_logout)

        self.patients.clicked.connect(self.patient_details)

        self.app.clicked.connect(self.appointment_list)

    def patient_logout(self):
        self.new_form = ViewBook3()
        self.new_form.show()
        self.close()

    def appointment_list(self):
        self.new_form = Appointments()
        self.new_form.show()
        self.close()

    def patient_details(self):
        self.new_form = Patient_Records("doctor")
        self.new_form.show()
        self.close()

# 8patient homepage
class Patient_homepage(QtWidgets.QMainWindow):  
    def __init__(self, email):
        super(Patient_homepage, self).__init__() 
        uic.loadUi('patienthomeFINAL2.0.ui', self) 
        self.setWindowTitle("Patient Homepage")

        self.email = email
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()

        self.logout_patient.clicked.connect(self.patient_logout)

        self.book_app.clicked.connect(self.book_appointment)

        self.view_my_rec.clicked.connect(self.private_records)

    def patient_logout(self):
        self.new_form = ViewBook3()
        self.new_form.show()
        self.close()

    def private_records(self):
        self.new_form = Private_view_patient(self.email)
        self.new_form.show()
        self.close()
    
    def book_appointment(self):
        self.new_form = Appointments_booking()
        self.new_form.show()
        self.close()

# 9patient list
class Patient_Records(QtWidgets.QMainWindow):  
    def __init__(self,user):
        super(Patient_Records, self).__init__() 
        uic.loadUi('patient_records.ui', self) 
        self.setWindowTitle("Patient List")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()
        self.user = user
        print(self.user)
        
        self.search_patient.clicked.connect(self.search_pat)

        self.back_button.clicked.connect(self.back_to_dochome)

        self.view_button.clicked.connect(self.patient_history)

        self.populate_table()

    def back_to_dochome(self):
        if self.user == 'admin':
            print('line460')
            self.new_form1 = Admin_homepage("admin") 
            self.new_form1.show()
      
        elif self.user == 'doctor':
            self.new_form2 = Doctor_homepage("doctor")
            self.new_form2.show()
      
        self.close()

    def patient_history(self):
        chosen_row = self.tableWidget.currentRow()
        
        if chosen_row != -1:
            firstname= self.tableWidget.item(chosen_row,0).text()
            p_contact = self.tableWidget.item(chosen_row,4).text()
            print(firstname,p_contact)
            
            
        self.new_form = Patient_History(self.user,firstname,p_contact)
        self.new_form.show()
        self.close()

    def search_pat(self):
        inputname = self.patient_name.text().lower()
        
        new_lst=[]

        for row in range(self.tableWidget.rowCount()):
            table_name = self.tableWidget.item(row, 0).text().lower()

            # Check if the table name starts with the input name
            if table_name.startswith(inputname):
                # Append the entire row data
                new_lst.append([self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())])

        self.tableWidget.clear()

        # self.booksTableWidget.setRowCount(len(new_lst))
        for i in range(len(new_lst)):
            for j in range(5):
                item = QTableWidgetItem(new_lst[i][j])
                # Make the items non-editable
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.tableWidget.setItem(i, j, item)

    def populate_table(self):
        # Create the connection string based on the authentication method chosen
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        # TODO: Write SQL query to fetch orders data
        cursor.execute("""
                    SELECT 
                    first_name+' '+last_name,
                    year(GETDATE()) - year(DOB) as age,
                    (SELECT TOP 1 gender FROM gender WHERE patients.gender_id = gender.gender_id) AS gender,
                    DOB,
                    contact
                FROM patients;

                """)
        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.tableWidget.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust content display
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        

    
# 10expanded patient history
class Patient_History(QtWidgets.QMainWindow):  
    def __init__(self,user,firstname,p_contact):
        super(Patient_History, self).__init__() 
        uic.loadUi('patient_details.ui', self) 
        self.setWindowTitle("Patient History")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
        self.appoint_ids = []

        self.show()
        self.user = user

        self.back_to_rec.clicked.connect(self.back_to_list)
        self.populate_screen(firstname,p_contact)
        
        # self.checkBox_6.clear()

    def back_to_list(self):
        self.new_form = Patient_Records(self.user)
        self.new_form.show()
        self.close()
        
    def populate_screen(self,firstname,p_contact):
        # Create the connection string based on the authentication method chosen
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        # TODO: Write SQL query to fetch orders data
        cursor.execute("""
                    select first_name,last_name,email,DOB,contact,emergency_contact,year(GETDATE()) - year(DOB) as age,gender,patient_weight,patient_id from patients join gender on patients.gender_id=gender.gender_id where first_name+' '+last_name = ? and contact = ?

                """,firstname,p_contact)
        
        patient_info = cursor.fetchall()
        # print(patient_info)
        
        if patient_info:
            self.lineEdit_14.setText(str(patient_info[0][2]))
            self.lineEdit_3.setText(str(patient_info[0][0]))
            self.lineEdit_5.setText(str(patient_info[0][1]))
            self.lineEdit_2.setText(str(patient_info[0][7]))
            self.lineEdit_4.setText(str(patient_info[0][6]))
            self.lineEdit_11.setText(str(patient_info[0][4]))
            self.lineEdit_12.setText(str(patient_info[0][5]))
            self.lineEdit_15.setText(str(patient_info[0][3]))
            self.lineEdit_18.setText(str(patient_info[0][8]))

            
        else:
            print('no')
        
        patientid = patient_info[0][-1]

        cursor.execute("""
            SELECT P.patient_id, A.appointment_id, COUNT(P.patient_id) as visitNumbers
            FROM Patients P
            JOIN Appointments_booked A ON P.patient_id = A.patient_id
            WHERE P.patient_id = ?
            GROUP BY P.patient_id, A.appointment_id;
        """, patientid)

        patient_appointments = cursor.fetchall()
        print(patient_appointments)
        
        
        # appoint_ids = []
        self.appoint_ids = []
        if patient_appointments:
            # Assuming you want to process the results in some way
            for row in patient_appointments:
                patient_id = row.patient_id
                appointment_id = row.appointment_id
                self.appoint_ids.append(appointment_id)
                visit_numbers = row.visitNumbers

        # Now you can use patient_appointments to populate your ComboBox or perform other actions
            no_of_visits = len(patient_appointments)
            for i in range(1, no_of_visits + 1):
                self.comboBox.addItem(str(i))
            # print(appoint_ids)
        else:
            print('No appointments found for the specified patient.')
            
        self.search_details.clicked.connect(self.get_selected_text)
        
        # Close the database connection
        connection.close()
        
    def get_selected_text(self):
        selected_text = self.comboBox.currentText()
        print(f"Selected Text: {selected_text}")
        iteration_num=int(selected_text)-1
        corresponding_appointment_id=self.appoint_ids[iteration_num]
        # print(corresponding_appointment_id)
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        self.listWidget_4.clear()
        self.lineEdit_10.clear()
        self.checkBox_6.setChecked(False)
        self.checkBox.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.lineEdit_19.clear()
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        self.radioButton_5.setChecked(False)
        self.radioButton_6.setChecked(False)
        self.radioButton_9.setChecked(False)
        self.radioButton_10.setChecked(False)
        self.radioButton_11.setChecked(False)
        self.radioButton_8.setChecked(False)

        
        # Create the connection string based on the authentication method chosen
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        # TODO: Write SQL query to fetch orders data
        cursor.execute("""
                    select symptoms from appointments_booked a join patient_record_symptoms s on a.appointment_id = s.appointment_id where a.appointment_id = ?
                """,corresponding_appointment_id)
        
        all_symptoms = cursor.fetchall()
        # print(all_symptoms)
        for row in all_symptoms:
                self.listWidget.addItem(row.symptoms)
                
                
        cursor.execute("""
                    select diagnosis from appointments_booked a join patient_record_diagnosis s on a.appointment_id = s.appointment_id where a.appointment_id = ?
                """,corresponding_appointment_id)
        
        all_diagnosis = cursor.fetchall()
        # print(all_symptoms)
        for row in all_diagnosis:
                self.listWidget_3.addItem(row.diagnosis)
                
        
        cursor.execute("""
                    select allergies from appointments_booked a join patient_record_allergies s on a.appointment_id = s.appointment_id where a.appointment_id = ?
                """,corresponding_appointment_id)
        
        all_allergies = cursor.fetchall()
        # print(all_symptoms)
        for row in all_allergies:
                self.listWidget_2.addItem(row.allergies)
                
                
        cursor.execute("""
                    select doctors_advice,medicine from appointments_booked a join prescriptions s on a.appointment_id = s.appointment_id where a.appointment_id = ?
                """,corresponding_appointment_id)
        
        all_treatments = cursor.fetchall()
        # print(all_symptoms)
        for row in all_treatments:
                self.listWidget_4.addItem(row.doctors_advice)
                self.listWidget_4.addItem(row.medicine)
                
                
        cursor.execute("""
                    select a.appointment_id,a.is_admitted,a.room_num from appointments_booked a join patients p on a.patient_id=p.patient_id where p.patient_id=?
                """,corresponding_appointment_id)
        
        admitted = cursor.fetchall()
        print(admitted)
        if admitted:
                is_admitted = admitted[0].is_admitted
                print(is_admitted)
                self.checkBox_6.setChecked(is_admitted)
                if is_admitted==True:
                    self.lineEdit_10.setText(str(admitted[0].room_num))
        else:
            print("No admission status found for the selected appointment.")
            
            
        cursor.execute("""
                    select a.appointment_id,reason from reason_for_visit r join appointments_booked a on r.appointment_id=a.appointment_id where a.appointment_id=?
                """,corresponding_appointment_id)
        
        reasons = cursor.fetchall()
        
        for reason in reasons:
            if reason[1] == 'Counselling':
                self.checkBox.setChecked(True)
            elif reason[1]== 'Psychotherapy':
                self.checkBox_4.setChecked(True)
            elif reason[1] == 'Regular Sessions':
                self.checkBox_5.setChecked(True)
            else:
                self.lineEdit_19.setText(reason[1])
                
        cursor.execute("""
                    select status,outcome,appointment_id from appointments_booked where appointment_id =?
                """,corresponding_appointment_id)
        
        status_outcome = cursor.fetchall()
        status = status_outcome[0][0]
        if status == 'Significant Improvement':
            self.radioButton_2.setChecked(True)
        elif status== 'Mild Improvement':
            self.radioButton_4.setChecked(True)
        elif status == 'Moderate Improvement':
            self.radioButton_3.setChecked(True)
        elif status == 'No Change':
            self.radioButton_5.setChecked(True)
        elif status == 'Condition Worsened':
            self.radioButton_6.setChecked(True)
            
        outcome = status_outcome[0][1]
        if outcome == 'Discharged':
            self.radioButton_9.setChecked(True)
        elif outcome== 'Lost for follow-Up':
            self.radioButton_10.setChecked(True)
        elif outcome == 'Transfer':
            self.radioButton_11.setChecked(True)
        elif outcome == 'Death':
            self.radioButton_8.setChecked(True)

                
        # Close the database connection
        connection.close()

# 11appointment list
class Appointments(QtWidgets.QMainWindow):  
    def __init__(self):
        super(Appointments, self).__init__() 
        uic.loadUi('updated_appointments.ui', self) 
        self.setWindowTitle("Appointments List")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()
        
        self.search_app.clicked.connect(self.search_appointments)
        self.back_to_doc_home.clicked.connect(self.backtohome)

        self.view_app_details.clicked.connect(self.appointment_expanded)
        self.populate_appointment_table()

    def appointment_expanded(self):
        chosen_row = self.apptable.currentRow()
        # chosen_row = self.apptable.currentRow()
        
        if chosen_row != -1:
            
            name = self.apptable.item(chosen_row, 0).text()
            # contact = cursor.fetchall()
            time = self.apptable.item(chosen_row, 2).text()
            day = self.apptable.item(chosen_row, 3).text()
            cancelled=eval(self.apptable.item(chosen_row, 4).text())
            print(name,time,day,cancelled)

        self.new_form = Appointments_details(name, time, day, cancelled)
        self.new_form.show()
        self.close()

    def backtohome(self):
        self.new_form = Doctor_homepage("doctor")
        self.new_form.show()
        self.close()
        
    def search_appointments(self):
        name_input = self.patient_app.text().lower()

        new_lst = []

        for row in range(self.apptable.rowCount()):
            table_name = self.apptable.item(row, 0).text().lower()
            
            if table_name == name_input:
                new_lst.append([self.apptable.item(row, col).text() for col in range(self.apptable.columnCount())])

        # Clear the table and set the row count
        self.apptable.clear()
        self.apptable.setRowCount(len(new_lst))

        # Populate the table with the new data
        for i in range(len(new_lst)):
            for j in range(self.apptable.columnCount()):
                item = QtWidgets.QTableWidgetItem(new_lst[i][j])
                # Make the items non-editable
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.apptable.setItem(i, j, item)

    def populate_appointment_table(self):
        # Create the connection string based on the authentication method chosen
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        # TODO: Write SQL query to fetch orders data
        cursor.execute("""
                        select p.first_name + ' ' + p.last_name AS patient_name,d.first_name + ' ' + d.last_name AS doctor_name,s.start_time,s.day,a.cancel_appointment from patients p join appointments_booked a on p.patient_id=a.patient_id join slots_available s on s.slot_id=a.slot_id join doctor d on d.doctor_id=s.doctor_id

                    """)
        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.apptable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.apptable.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust content display
        header = self.apptable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)


# 12expanded appointment details
class Appointments_details(QtWidgets.QMainWindow):  
    def __init__(self, name, time, day, cancelled):
        super(Appointments_details, self).__init__() 
        uic.loadUi('appointment_details.ui', self) 
        self.setWindowTitle("Appointment Details")
        
        self.lineEdit.setText(name)
        self.lineEdit_3.setText(time)
        self.lineEdit_5.setText(day)
        self.checkBox_2.setChecked(cancelled)

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()

        self.back_to_app_list.clicked.connect(self.back_to_applist)

        # self.pat_history.clicked.connect(self.viewhistory)

        self.edit_history.clicked.connect(self.patient_his_editable)

        self.insert_contact(name)
        
        # self.search_appointment_and_update_date(name)
        
    def insert_contact(self, patient_name):
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
            connection = pyodbc.connect(connection_string)

            cursor = connection.cursor()

            
            cursor.execute("""
                SELECT contact
                FROM patients
                WHERE first_name + ' ' + last_name = ?;
            """, patient_name)

            contact_info = cursor.fetchall()

            if contact_info:
                # Fetch the contact information from the result
                contact_value = contact_info[0][0]
                # print(contact_value)

                # Clear existing text in the line edit (assuming self.lineEditContact is your line edit widget)
                self.lineEdit_2.clear()

                # Set the contact information in the line edit
                self.lineEdit_2.setText(str(contact_value))

            else:
                # Handle the case where no contact information is found
                self.lineEdit_2.clear()
                # Optionally, display a message or take other appropriate actions

            connection.close()  # Make sure to close the connection even if an exception occurs


    # def viewhistory(self):
        
    #     patient_name = self.lineEdit.text()
    #     print(patient_name)
        
    #     connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    #     connection = pyodbc.connect(connection_string)
        
    #     cursor = connection.cursor()

    #     cursor.execute("""
    #         SELECT patient_id
    #         FROM patients
    #         WHERE first_name + ' ' + last_name = ?;
    #     """, patient_name)

    #     contact_info = cursor.fetchall()
    #     id = contact_info[0][0]
    
    #     self.new_form = app_view_doc(id)
    #     self.new_form.show()
    #     self.close()
        
    def back_to_applist(self):
        self.new_form = Appointments()
        self.new_form.show()
        self.close()

    def patient_his_editable(self):
        self.new_form = editable_patient_history()
        self.new_form.show()
        
# 13slots available booking
class Appointments_booking(QtWidgets.QMainWindow):  
    def __init__(self):
        super(Appointments_booking, self).__init__() 
        uic.loadUi('patientappointment.ui', self) 
        self.setWindowTitle("Slots Available")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()

        self.back_to_booking.clicked.connect(self.backtobooking)

        self.booking_done.clicked.connect(self.app_booked)

        self.populate_combobox()
        self.comboBox.currentIndexChanged.connect(self.populate_listWidget)
        self.comboBox.currentIndexChanged.connect(self.populate_comboBox_2)
        self.comboBox.currentIndexChanged.connect(self.populate_comboBox_4)
        self.comboBox.currentIndexChanged.connect(self.populate_comboBox_5)
        # Connect the method to the currentIndexChanged signals of comboBox_2, comboBox_4, and comboBox_5
        self.comboBox_2.currentIndexChanged.connect(self.update_day_line_edit)
        self.comboBox_4.currentIndexChanged.connect(self.update_day_line_edit)
        self.comboBox_5.currentIndexChanged.connect(self.update_day_line_edit)
        self.comboBox_2.currentIndexChanged.connect(self.update_slots_combo_box)
        self.comboBox_4.currentIndexChanged.connect(self.update_slots_combo_box)
        self.comboBox_5.currentIndexChanged.connect(self.update_slots_combo_box)
        self.lineEdit.textChanged.connect(self.update_slots_combo_box)

    def backtobooking(self):
    # Create an instance of Patient_homepage by passing the email parameter
        self.new_form = Patient_homepage(self.email)
        self.new_form.show()
        self.close()

    def app_booked(self):
        output=QMessageBox(self)              
        output.setWindowTitle("Appointment") 
        output.setText("Your appointment has been successfully booked!.")
        output.setStandardButtons( QMessageBox.StandardButton.Ok)
        output.setIcon(QMessageBox.Icon.Information) 
        button=output.exec()
        self.close()
        
    def populate_combobox(self):
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
            connection = pyodbc.connect(connection_string)
            
            cursor = connection.cursor()
            cursor.execute("""
                        SELECT first_name+' '+last_name as doctor_name from doctor

                    """)
            
            doctor_names = cursor.fetchall()

            # Populate the ComboBox with doctor names
            for doctor_name in doctor_names:
                self.comboBox.addItem(doctor_name.doctor_name)

            connection.close()

    def populate_listWidget(self):
        # Your existing code for database connection...
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()
        selected_text = self.comboBox.currentText()
        first_name = selected_text.split()[0]
        last_name = selected_text.split()[1]
        cursor.execute("""
                    SELECT s.specialization
                    FROM doctor d
                    JOIN doctorspecialization ds ON d.doctor_id = ds.doctor_id
                    JOIN specialization s ON ds.specialization_id = s.specialization_id
                    WHERE d.first_name = ? AND d.last_name = ?;
                """, first_name, last_name)

        specialization_names = cursor.fetchall()

        # Clear the existing items in the listWidget
        self.listWidget.clear()

        for result in specialization_names:
            item = QtWidgets.QListWidgetItem(str(result[0]))  # Assuming your result is a single column, adjust the index accordingly
            self.listWidget.addItem(item)

    def populate_comboBox_2(self):
        # populate according to current text
        # Assuming you have the doctor's name selected in comboBox
        selected_doctor_name = self.comboBox.currentText()

        # Split the doctor's name into first name and last name
        doctor_first_name = selected_doctor_name.split()[0]
        doctor_last_name = selected_doctor_name.split()[1]

        # Query to fetch available years for the selected doctor's slots
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Execute the query
        cursor.execute("""
            SELECT DISTINCT year
            FROM slots_available sa
            JOIN doctor d ON sa.doctor_id = d.doctor_id
            WHERE d.first_name = ? AND d.last_name = ?;
        """, doctor_first_name, doctor_last_name)

        # Fetch the results
        available_years = cursor.fetchall()

        # Clear existing items in comboBox_2
        self.comboBox_2.clear()

        # Populate comboBox_2 with available years
        for year in available_years:
            self.comboBox_2.addItem(str(year[0]))  # Assuming the result is a single column, adjust the index accordingly

        # Close the database connection
        connection.close()

    def populate_comboBox_4(self):
    # Assuming you have the doctor's name selected in comboBox
        selected_doctor_name = self.comboBox.currentText()

        # Split the doctor's name into first name and last name
        doctor_first_name = selected_doctor_name.split()[0]
        doctor_last_name = selected_doctor_name.split()[1]

        # Query to fetch available months for the selected doctor's slots
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Execute the query
        cursor.execute("""
            SELECT DISTINCT month
            FROM slots_available sa
            JOIN doctor d ON sa.doctor_id = d.doctor_id
            WHERE d.first_name = ? AND d.last_name = ?;
        """, doctor_first_name, doctor_last_name)

        # Fetch the results
        available_months = cursor.fetchall()

        # Clear existing items in comboBox_3
        self.comboBox_4.clear()

        # Populate comboBox_3 with available months
        for month in available_months:
            self.comboBox_4.addItem(str(month[0]))  # Assuming the result is a single column, adjust the index accordingly

        # Close the database connection
        connection.close()

    def populate_comboBox_5(self):
    # Assuming you have the doctor's name selected in comboBox
        selected_doctor_name = self.comboBox.currentText()

        # Split the doctor's name into first name and last name
        doctor_first_name = selected_doctor_name.split()[0]
        doctor_last_name = selected_doctor_name.split()[1]

        # Query to fetch available months for the selected doctor's slots
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Execute the query
        cursor.execute("""
    SELECT DISTINCT dateday
    FROM slots_available sa
    JOIN doctor d ON sa.doctor_id = d.doctor_id
    WHERE d.first_name = ? AND d.last_name = ?;
""", doctor_first_name, doctor_last_name)
        # Fetch the results
        available_months = cursor.fetchall()

        # Clear existing items in comboBox_3
        self.comboBox_5.clear()

        # Populate comboBox_3 with available months
        for month in available_months:
            self.comboBox_5.addItem(str(month[0]))  # Assuming the result is a single column, adjust the index accordingly

        # Close the database connection
        connection.close()

    def update_day_line_edit(self):
    # Get the selected values from comboBox_2, comboBox_4, and comboBox_5
        selected_year = self.comboBox_2.currentText()
        selected_month = self.comboBox_4.currentText()
        selected_date = self.comboBox_5.currentText()

        # Ensure that all values are selected
        if selected_year and selected_month and selected_date:
            # Split the doctor's name into first name and last name
            selected_doctor_name = self.comboBox.currentText()
            doctor_first_name = selected_doctor_name.split()[0]
            doctor_last_name = selected_doctor_name.split()[1]

            # Query to fetch the day for the selected date
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            # Execute the query
            cursor.execute("""
                SELECT day
                FROM slots_available sa
                JOIN doctor d ON sa.doctor_id = d.doctor_id
                WHERE d.first_name = ? AND d.last_name = ? AND sa.year = ? AND sa.month = ? AND sa.dateday = ?;
            """, doctor_first_name, doctor_last_name, selected_year, selected_month, selected_date)

            # Fetch the result
            day_result = cursor.fetchone()

            # Update the day_line_edit with the fetched day
            if day_result:
                self.lineEdit.setText(day_result[0])

            # Close the database connection
            connection.close()

    def update_slots_combo_box(self):
    # Get the selected values from comboBox_2, comboBox_4, and comboBox_5
        selected_year = self.comboBox_2.currentText()
        selected_month = self.comboBox_4.currentText()
        selected_date = self.comboBox_5.currentText()

        # Ensure that all values are selected
        if selected_year and selected_month and selected_date:
            # Split the doctor's name into first name and last name
            selected_doctor_name = self.comboBox.currentText()
            doctor_first_name = selected_doctor_name.split()[0]
            doctor_last_name = selected_doctor_name.split()[1]

            # Get the selected day
            selected_day = self.lineEdit.text()

            # Query to fetch available slots for the selected day, date, and doctor
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            # Execute the query
            cursor.execute("""
    SELECT start_time, end_time
    FROM slots_available sa
    JOIN doctor d ON sa.doctor_id = d.doctor_id
    WHERE d.first_name = ? AND d.last_name = ? 
        AND sa.year = ? AND sa.month = ? AND sa.dateday = ?;
""", (doctor_first_name, doctor_last_name, selected_year, selected_month, selected_date))

            # Fetch the results
            available_slots = cursor.fetchall()

            # Clear existing items in comboBox_3
            self.comboBox_3.clear()

            # Populate comboBox_3 with available slots
            for slot in available_slots:
                slot_time_range = f"{slot.start_time} - {slot.end_time}"
                self.comboBox_3.addItem(slot_time_range)

            # Close the database connection
            connection.close()

# 14patient history private veiw for patient
class Private_view_patient(QtWidgets.QMainWindow):  
    def __init__(self, email):
        super(Private_view_patient, self).__init__() 
        uic.loadUi('patient_details(patient_view).ui', self) 
        self.setWindowTitle("Patient History")

        self.email = email
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()

        self.back_to_rec.clicked.connect(self.back_patienthome)
        self.populate_screen(email)

    def back_patienthome(self):
        self.new_form = Patient_homepage(self.email)
        self.new_form.show()
        self.close()

    def populate_screen(self,email):
        # Create the connection string based on the authentication method chosen
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        # TODO: Write SQL query to fetch orders data
        cursor.execute("""
                    select first_name,last_name,email,DOB,contact,emergency_contact,year(GETDATE()) - year(DOB) as age,gender,patient_weight,patient_id from patients join gender on patients.gender_id=gender.gender_id where email =?

                """,email)
        
        patient_info = cursor.fetchall()
        # print(patient_info)
        
        if patient_info:
            self.lineEdit_14.setText(str(patient_info[0][2]))
            self.lineEdit_3.setText(str(patient_info[0][0]))
            self.lineEdit_5.setText(str(patient_info[0][1]))
            self.lineEdit_2.setText(str(patient_info[0][7]))
            self.lineEdit_4.setText(str(patient_info[0][6]))
            self.lineEdit_11.setText(str(patient_info[0][4]))
            self.lineEdit_12.setText(str(patient_info[0][5]))
            self.lineEdit_15.setText(str(patient_info[0][3]))
            self.lineEdit_18.setText(str(patient_info[0][8]))

            
        else:
            print('no')
        
        # print(patient_info)
        patientid = patient_info[0][-1]

        cursor.execute("""
            SELECT P.patient_id, A.appointment_id, COUNT(P.patient_id) as visitNumbers
            FROM Patients P
            JOIN Appointments_booked A ON P.patient_id = A.patient_id
            WHERE P.patient_id = ?
            GROUP BY P.patient_id, A.appointment_id;
        """, patientid)

        patient_appointments = cursor.fetchall()
        print(patient_appointments)
        
        
        # appoint_ids = []
        self.appoint_ids = []
        if patient_appointments:
            # Assuming you want to process the results in some way
            for row in patient_appointments:
                patient_id = row.patient_id
                appointment_id = row.appointment_id
                self.appoint_ids.append(appointment_id)
                visit_numbers = row.visitNumbers

        # Now you can use patient_appointments to populate your ComboBox or perform other actions
            no_of_visits = len(patient_appointments)
            for i in range(1, no_of_visits + 1):
                self.comboBox.addItem(str(i))
            # print(appoint_ids)
        else:
            print('No appointments found for the specified patient.')
            
        self.search_details.clicked.connect(self.get_selected_text)
        
        # Close the database connection
        connection.close()
        
    def get_selected_text(self):
        selected_text = self.comboBox.currentText()
        print(f"Selected Text: {selected_text}")
        iteration_num=int(selected_text)-1
        corresponding_appointment_id=self.appoint_ids[iteration_num]
        # print(corresponding_appointment_id)
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        self.listWidget_4.clear()
        self.lineEdit_10.clear()
        self.checkBox_6.setChecked(False)
        self.checkBox.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.lineEdit_19.clear()
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        self.radioButton_5.setChecked(False)
        self.radioButton_6.setChecked(False)
        self.radioButton_9.setChecked(False)
        self.radioButton_10.setChecked(False)
        self.radioButton_11.setChecked(False)
        self.radioButton_8.setChecked(False)

        
        # Create the connection string based on the authentication method chosen
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        # TODO: Write SQL query to fetch orders data
        cursor.execute("""
                    select symptoms from appointments_booked a join patient_record_symptoms s on a.appointment_id = s.appointment_id where a.appointment_id = ?
                """,corresponding_appointment_id)
        
        all_symptoms = cursor.fetchall()
        # print(all_symptoms)
        for row in all_symptoms:
                self.listWidget.addItem(row.symptoms)
                
                
        cursor.execute("""
                    select diagnosis from appointments_booked a join patient_record_diagnosis s on a.appointment_id = s.appointment_id where a.appointment_id = ?
                """,corresponding_appointment_id)
        
        all_diagnosis = cursor.fetchall()
        # print(all_symptoms)
        for row in all_diagnosis:
                self.listWidget_3.addItem(row.diagnosis)
                
        
        cursor.execute("""
                    select allergies from appointments_booked a join patient_record_allergies s on a.appointment_id = s.appointment_id where a.appointment_id = ?
                """,corresponding_appointment_id)
        
        all_allergies = cursor.fetchall()
        # print(all_symptoms)
        for row in all_allergies:
                self.listWidget_2.addItem(row.allergies)
                
                
        cursor.execute("""
                    select doctors_advice,medicine from appointments_booked a join prescriptions s on a.appointment_id = s.appointment_id where a.appointment_id = ?
                """,corresponding_appointment_id)
        
        all_treatments = cursor.fetchall()
        # print(all_symptoms)
        for row in all_treatments:
                self.listWidget_4.addItem(row.doctors_advice)
                self.listWidget_4.addItem(row.medicine)
                
                
        cursor.execute("""
                    select a.appointment_id,a.is_admitted,a.room_num from appointments_booked a join patients p on a.patient_id=p.patient_id where p.patient_id=?
                """,corresponding_appointment_id)
        
        admitted = cursor.fetchall()
        print(admitted)
        if admitted:
                is_admitted = admitted[0].is_admitted
                print(is_admitted)
                self.checkBox_6.setChecked(is_admitted)
                if is_admitted==True:
                    self.lineEdit_10.setText(str(admitted[0].room_num))
        else:
            print("No admission status found for the selected appointment.")
            
            
        cursor.execute("""
                    select a.appointment_id,reason from reason_for_visit r join appointments_booked a on r.appointment_id=a.appointment_id where a.appointment_id=?
                """,corresponding_appointment_id)
        
        reasons = cursor.fetchall()
        
        for reason in reasons:
            if reason[1] == 'Counselling':
                self.checkBox.setChecked(True)
            elif reason[1]== 'Psychotherapy':
                self.checkBox_4.setChecked(True)
            elif reason[1] == 'Regular Sessions':
                self.checkBox_5.setChecked(True)
            else:
                self.lineEdit_19.setText(reason[1])
                
        cursor.execute("""
                    select status,outcome,appointment_id from appointments_booked where appointment_id =?
                """,corresponding_appointment_id)
        
        status_outcome = cursor.fetchall()
        status = status_outcome[0][0]
        if status == 'Significant Improvement':
            self.radioButton_2.setChecked(True)
        elif status== 'Mild Improvement':
            self.radioButton_4.setChecked(True)
        elif status == 'Moderate Improvement':
            self.radioButton_3.setChecked(True)
        elif status == 'No Change':
            self.radioButton_5.setChecked(True)
        elif status == 'Condition Worsened':
            self.radioButton_6.setChecked(True)
            
        outcome = status_outcome[0][1]
        if outcome == 'Discharged':
            self.radioButton_9.setChecked(True)
        elif outcome== 'Lost for follow-Up':
            self.radioButton_10.setChecked(True)
        elif outcome == 'Transfer':
            self.radioButton_11.setChecked(True)
        elif outcome == 'Death':
            self.radioButton_8.setChecked(True)

                
        # Close the database connection
        connection.close()



# 15appointments list view for doctor
class app_view_doc(QtWidgets.QMainWindow):  
    def __init__(self,id):
        super(app_view_doc, self).__init__() 
        uic.loadUi('patient_details(doc_view).ui', self) 
        self.setWindowTitle("Patient History")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
        self.appoint_ids = []

        self.show()

        self.back_to_rec.clicked.connect(self.back_to_appointments)
        self.populate_screen(id)
        
    def back_to_appointments(self):
        self.new_form = Appointments_details()
        self.new_form.show()
        self.close()
    
    def populate_screen(self,id):
        # Create the connection string based on the authentication method chosen
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        # TODO: Write SQL query to fetch orders data
        cursor.execute("""
                    select first_name,last_name,email,DOB,contact,emergency_contact,year(GETDATE()) - year(DOB) as age,gender,patient_weight,patient_id from patients join gender on patients.gender_id=gender.gender_id where patient_id =?

                """,id)
        
        patient_info = cursor.fetchall()
        
        if patient_info:
            self.lineEdit_14.setText(str(patient_info[0][2]))
            self.lineEdit_3.setText(str(patient_info[0][0]))
            self.lineEdit_5.setText(str(patient_info[0][1]))
            self.lineEdit_2.setText(str(patient_info[0][7]))
            self.lineEdit_4.setText(str(patient_info[0][6]))
            self.lineEdit_11.setText(str(patient_info[0][4]))
            self.lineEdit_12.setText(str(patient_info[0][5]))
            self.lineEdit_15.setText(str(patient_info[0][3]))
            self.lineEdit_18.setText(str(patient_info[0][8]))

            
        else:
            print('no')
        
        patientid = patient_info[0][-1]

        cursor.execute("""
            SELECT P.patient_id, A.appointment_id, COUNT(P.patient_id) as visitNumbers
            FROM Patients P
            JOIN Appointments_booked A ON P.patient_id = A.patient_id
            WHERE P.patient_id = ?
            GROUP BY P.patient_id, A.appointment_id;
        """, patientid)

        patient_appointments = cursor.fetchall()
        print(patient_appointments)
        
        
        # appoint_ids = []
        self.appoint_ids = []
        if patient_appointments:
            # Assuming you want to process the results in some way
            for row in patient_appointments:
                patient_id = row.patient_id
                appointment_id = row.appointment_id
                self.appoint_ids.append(appointment_id)
                visit_numbers = row.visitNumbers

        # Now you can use patient_appointments to populate your ComboBox or perform other actions
            no_of_visits = len(patient_appointments)
            for i in range(1, no_of_visits + 1):
                self.comboBox.addItem(str(i))
            # print(appoint_ids)
        else:
            print('No appointments found for the specified patient.')
            
        self.search_details.clicked.connect(self.get_selected_text)
        
        # Close the database connection
        connection.close()
        
    def get_selected_text(self):
        selected_text = self.comboBox.currentText()
        print(f"Selected Text: {selected_text}")
        iteration_num=int(selected_text)-1
        corresponding_appointment_id=self.appoint_ids[iteration_num]
        # print(corresponding_appointment_id)
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        self.listWidget_4.clear()
        self.lineEdit_10.clear()
        self.checkBox_6.setChecked(False)
        self.checkBox.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.lineEdit_19.clear()
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        self.radioButton_5.setChecked(False)
        self.radioButton_6.setChecked(False)
        self.radioButton_9.setChecked(False)
        self.radioButton_10.setChecked(False)
        self.radioButton_11.setChecked(False)
        self.radioButton_8.setChecked(False)

        
        # Create the connection string based on the authentication method chosen
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        # TODO: Write SQL query to fetch orders data
        cursor.execute("""
                    select symptoms from appointments_booked a join patient_record_symptoms s on a.appointment_id = s.appointment_id where a.appointment_id = ?
                """,corresponding_appointment_id)
        
        all_symptoms = cursor.fetchall()
        # print(all_symptoms)
        for row in all_symptoms:
                self.listWidget.addItem(row.symptoms)
                
                
        cursor.execute("""
                    select diagnosis from appointments_booked a join patient_record_diagnosis s on a.appointment_id = s.appointment_id where a.appointment_id = ?
                """,corresponding_appointment_id)
        
        all_diagnosis = cursor.fetchall()
        # print(all_symptoms)
        for row in all_diagnosis:
                self.listWidget_3.addItem(row.diagnosis)
                
        
        cursor.execute("""
                    select allergies from appointments_booked a join patient_record_allergies s on a.appointment_id = s.appointment_id where a.appointment_id = ?
                """,corresponding_appointment_id)
        
        all_allergies = cursor.fetchall()
        # print(all_symptoms)
        for row in all_allergies:
                self.listWidget_2.addItem(row.allergies)
                
                
        cursor.execute("""
                    select doctors_advice,medicine from appointments_booked a join prescriptions s on a.appointment_id = s.appointment_id where a.appointment_id = ?
                """,corresponding_appointment_id)
        
        all_treatments = cursor.fetchall()
        # print(all_symptoms)
        for row in all_treatments:
                self.listWidget_4.addItem(row.doctors_advice)
                self.listWidget_4.addItem(row.medicine)
                
                
        cursor.execute("""
                    select a.appointment_id,a.is_admitted,a.room_num from appointments_booked a join patients p on a.patient_id=p.patient_id where p.patient_id=?
                """,corresponding_appointment_id)
        
        admitted = cursor.fetchall()
        print(admitted)
        if admitted:
                is_admitted = admitted[0].is_admitted
                print(is_admitted)
                self.checkBox_6.setChecked(is_admitted)
                if is_admitted==True:
                    self.lineEdit_10.setText(str(admitted[0].room_num))
        else:
            print("No admission status found for the selected appointment.")
            
            
        cursor.execute("""
                    select a.appointment_id,reason from reason_for_visit r join appointments_booked a on r.appointment_id=a.appointment_id where a.appointment_id=?
                """,corresponding_appointment_id)
        
        reasons = cursor.fetchall()
        
        for reason in reasons:
            if reason[1] == 'Counselling':
                self.checkBox.setChecked(True)
            elif reason[1]== 'Psychotherapy':
                self.checkBox_4.setChecked(True)
            elif reason[1] == 'Regular Sessions':
                self.checkBox_5.setChecked(True)
            else:
                self.lineEdit_19.setText(reason[1])
                
        cursor.execute("""
                    select status,outcome,appointment_id from appointments_booked where appointment_id =?
                """,corresponding_appointment_id)
        
        status_outcome = cursor.fetchall()
        status = status_outcome[0][0]
        if status == 'Significant Improvement':
            self.radioButton_2.setChecked(True)
        elif status== 'Mild Improvement':
            self.radioButton_4.setChecked(True)
        elif status == 'Moderate Improvement':
            self.radioButton_3.setChecked(True)
        elif status == 'No Change':
            self.radioButton_5.setChecked(True)
        elif status == 'Condition Worsened':
            self.radioButton_6.setChecked(True)
            
        outcome = status_outcome[0][1]
        if outcome == 'Discharged':
            self.radioButton_9.setChecked(True)
        elif outcome== 'Lost for follow-Up':
            self.radioButton_10.setChecked(True)
        elif outcome == 'Transfer':
            self.radioButton_11.setChecked(True)
        elif outcome == 'Death':
            self.radioButton_8.setChecked(True)

                
        # Close the database connection
        connection.close()

# 16doctor list
class doctors_list(QtWidgets.QMainWindow):  
    def __init__(self):
        super(doctors_list, self).__init__() 
        uic.loadUi('Doctors_list.ui', self) 
        self.setWindowTitle("Doctors List")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()

        self.search_doc.clicked.connect(self.search_doctor)

        self.view_doc_details.clicked.connect(self.doc_information)

        self.back_to_adminhome.clicked.connect(self.go_back_adminhome)

        self.search_specialisation()

        self.populate_doctor_table()
    def doc_information(self):
        chosen_row = self.tableWidget.currentRow()
        if chosen_row>=0:
            name = self.tableWidget.item(chosen_row, 0).text()
            assigned_pod = self.tableWidget.item(chosen_row, 3).text()
            gender = self.tableWidget.item(chosen_row, 1).text()

            self.new_form = doctor_details(name, assigned_pod, gender)
            self.new_form.show()
            self.close()
    
    def go_back_adminhome(self):
        self.new_form = Admin_homepage('admin')
        self.new_form.show()
        self.close()

    def search_doctor(self):
        current_text = self.comboBox.currentText().lower()
        new_lst = []

        for row in range(self.tableWidget.rowCount()):
            table_name = self.tableWidget.item(row, 2).text().lower()
            
            if table_name == current_text:
                new_lst.append([self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())])

        # Clear the table
        self.tableWidget.clear()

        # Set the row count
        self.tableWidget.setRowCount(len(new_lst))

        # Populate the table with the new data
        for i in range(len(new_lst)):
            for j in range(self.tableWidget.columnCount()):
                item = QtWidgets.QTableWidgetItem(new_lst[i][j])
                # Make the items non-editable
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.tableWidget.setItem(i, j, item)

    def search_specialisation(self):
        # populates combobox 
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        
        cursor = connection.cursor()
        cursor.execute("""
                    SELECT * FROM specialization
                    """)
        # Fetch all rows and populate the table
        data_for_combobox = cursor.fetchall()

        # Close the database connection
        connection.close()

        # Populate the combobox with data
        for row_data in data_for_combobox:
            specialization = row_data[1]  # Assuming specialization is in the first column
            self.comboBox.addItem(specialization)

    def populate_doctor_table(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        
        cursor = connection.cursor()
        cursor.execute("""
                    SELECT 
                    d.first_name + ' ' + d.last_name AS doctor_name,
                    g.gender AS doctor_gender,
                    s.specialization AS doctor_specialization,
                    d.assigned_pod AS doctor_assigned_pod
                    FROM
                        doctor d
                    JOIN
                        gender g ON d.gender_id = g.gender_id
                    JOIN
                        doctorspecialization ds ON d.doctor_id = ds.doctor_id
                    JOIN
                        specialization s ON ds.specialization_id = s.specialization_id;

                    """)
        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.tableWidget.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust content display
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

# 17expanded doctor details
class doctor_details(QtWidgets.QMainWindow):  
    def __init__(self, name, assigned_pod, gender):
        super(doctor_details, self).__init__() 
        uic.loadUi('Doctor_details.ui', self) 
        self.setWindowTitle("Doctor Details")
        
        self.lineEdit.setText(name)
        self.lineEdit_9.setText(assigned_pod)
        self.lineEdit_2.setText(gender)

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()

        self.back_to_doclist.clicked.connect(self.doc_list_back)
        self.populate_listWidget(name)

        self.populate_cnic(name)

        self.populate_license(name)

        self.populate_email(name)

        self.populate_days(name)

        self.populate_timings()

    def doc_list_back(self):
        self.new_form = doctors_list()
        self.new_form.show()
        self.close()

    def populate_listWidget(self, doctor_name):
        # Your existing code for database connection...
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()

        # Assuming the doctor's name is in the format "First Last"
        first_name = doctor_name.split()[0]
        last_name = doctor_name.split()[1]

        # Pass parameters as a tuple in the execute method
        cursor.execute("""
                    SELECT s.specialization
                    FROM doctor d
                    JOIN doctorspecialization ds ON d.doctor_id = ds.doctor_id
                    JOIN specialization s ON ds.specialization_id = s.specialization_id
                    WHERE d.first_name = ? AND d.last_name = ?;
                """, (first_name, last_name))

        specialization_names = cursor.fetchall()

        # Clear the existing items in the listWidget
        self.listWidget.clear()

        for result in specialization_names:
            item = QtWidgets.QListWidgetItem(str(result[0]))  # Assuming your result is a single column, adjust the index accordingly
            self.listWidget.addItem(item)

        connection.close()

    def populate_cnic(self, doctor_name):
        try:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
            connection = pyodbc.connect(connection_string)

            # Create a cursor to interact with the database
            cursor = connection.cursor()

            first_name = doctor_name.split()[0]
            last_name = doctor_name.split()[1]

            cursor.execute("""
                SELECT d.CNIC FROM doctor d WHERE d.first_name = ? AND d.last_name = ?;
            """, (first_name, last_name))

            cnic = cursor.fetchone()

            if cnic:
                # Fetch the CNIC from the result
                cnic_value = cnic[0]

                # Clear existing text in the line edit
                self.lineEdit_4.clear()

                # Set the CNIC in the line edit
                self.lineEdit_4.setText(str(cnic_value))

            else:
                # Handle the case where no CNIC is found
                self.lineEdit_4.clear()
                # Optionally, display a message or take other appropriate actions

        except Exception as e:
            print("Error in populate_cnic:", e)

        finally:
            connection.close()  # Make sure to close the connection even if an exception occurs

    def populate_license(self, doctor_name):
        try:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
            connection = pyodbc.connect(connection_string)

            # Create a cursor to interact with the database
            cursor = connection.cursor()

            first_name = doctor_name.split()[0]
            last_name = doctor_name.split()[1]

            cursor.execute("""
                SELECT d.medical_license_num FROM doctor d WHERE d.first_name = ? AND d.last_name = ?;
            """, (first_name, last_name))

            license_number = cursor.fetchone()

            if license_number:
                # Fetch the license number from the result
                license_value = license_number[0]

                # Clear existing text in the line edit
                self.lineEdit_3.clear()

                # Set the license number in the line edit
                self.lineEdit_3.setText(str(license_value))

            else:
                # Handle the case where no license number is found
                self.lineEdit_3.clear()
                # Optionally, display a message or take other appropriate actions

        except Exception as e:
            print("Error in populate_license:", e)

        finally:
            connection.close()  # Make sure to close the connection even if an exception occurs

    def populate_email(self, doctor_name):
        try:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
            connection = pyodbc.connect(connection_string)

            # Create a cursor to interact with the database
            cursor = connection.cursor()

            first_name = doctor_name.split()[0]
            last_name = doctor_name.split()[1]

            cursor.execute("""
                SELECT d.email FROM doctor d WHERE d.first_name = ? AND d.last_name = ?;
            """, (first_name, last_name))

            email_address = cursor.fetchone()

            if email_address:
                # Fetch the email address from the result
                email_value = email_address[0]

                # Clear existing text in the line edit
                self.lineEdit_8.clear()

                # Set the email address in the line edit
                self.lineEdit_8.setText(email_value)

            else:
                # Handle the case where no email address is found
                self.lineEdit_8.clear()
                # Optionally, display a message or take other appropriate actions

        except Exception as e:
            print("Error in populate_email:", e)

        finally:
            connection.close()  # Make sure to close the connection even if an exception occurs

    def populate_days(self, doctor_name):
        try:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
            connection = pyodbc.connect(connection_string)

            # Create a cursor to interact with the database
            cursor = connection.cursor()

            first_name = doctor_name.split()[0]
            last_name = doctor_name.split()[1]

            cursor.execute("""
                SELECT DISTINCT day
                FROM slots_available sa
                JOIN doctor d ON sa.doctor_id = d.doctor_id
                WHERE d.first_name = ? AND d.last_name = ?;
            """, (first_name, last_name))

            available_days = cursor.fetchall()

            # Clear existing items in comboBox (assuming self.comboBox is your ComboBox widget)
            self.comboBox.clear()

            # Populate comboBox with available days
            for day in available_days:
                self.comboBox.addItem(day[0])  # Assuming the result is a single column, adjust the index accordingly

        except Exception as e:
            print("Error in populate_days:", e)

        finally:
            connection.close()  # Make sure to close the connection even if an exception occurs

    def populate_timings(self):
            selected_doctor_name = self.lineEdit.text()  # Assuming you have a line edit for doctor's name
            selected_day = self.comboBox.currentText()  # Assuming you have a ComboBox for days

            # Split the doctor's name into first name and last name
            names = selected_doctor_name.split()
            if len(names) == 2:
                doctor_first_name = names[0]
                doctor_last_name = names[1]

                connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()

                # Execute the query
                cursor.execute("""
                    SELECT start_time, end_time
                    FROM slots_available sa
                    JOIN doctor d ON sa.doctor_id = d.doctor_id
                    WHERE d.first_name = ? AND d.last_name = ? AND sa.day = ?;
                """, doctor_first_name, doctor_last_name, selected_day)

                available_slots = cursor.fetchall()

                # Clear existing items in comboBox_3 (assuming self.comboBox_3 is your ComboBox widget for timings)
                self.comboBox_3.clear()

                # Populate comboBox_3 with available slots
                for slot in available_slots:
                    start_time = slot[0].strftime("%H:%M")  # Format the time if needed
                    end_time = slot[1].strftime("%H:%M")  # Format the time if needed
                    time_range = f"{start_time} - {end_time}"
                    self.comboBox_3.addItem(time_range)

            else:
                # Handle the case where the doctor's name is not entered correctly
                # You might want to clear the comboBox_3 or display a message to the user

                connection.close()  # Make sure to close the connection even if an exception occurs


# 18payment screen
class payment_details(QtWidgets.QMainWindow):  
    def __init__(self):
        super(payment_details, self).__init__() 
        uic.loadUi('payment_admin.ui', self) 
        self.setWindowTitle("Payment Details Page")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
        self.show()

        self.search_payment.clicked.connect(self.search_pay)

        self.back_to_adminpage.clicked.connect(self.back_to_adminhome)
        
        self.populate_table()

    def back_to_adminhome(self):
        self.new_form = Admin_homepage("admin")
        self.new_form.show()
        self.close()
        
    def populate_table(self):
        # Create the connection string based on the authentication method chosen
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        # TODO: Write SQL query to fetch orders data
        cursor.execute("""
                    select P.first_name +' '+P.last_name  as PatientName, A.amount, M.payment_method, start_time,end_time from patients P join appointments_booked A on P.patient_id=A.patient_id
                    join payment_method M on A.payment_method_id= M.payment_method_id
                    join slots_available S on S.slot_id = A.slot_id""")
        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.tableWidget.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust content display
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def search_pay(self):
        name_input = self.patient_payment.text().lower()

        new_lst = []

        for row in range(self.tableWidget.rowCount()):
            table_name = self.tableWidget.item(row, 0).text().lower()
            
            if table_name.startswith(name_input):
                new_lst.append([self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())])

        # Clear the table and set the row count
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(new_lst))

        # Populate the table with the new data
        for i in range(len(new_lst)):
            for j in range(self.tableWidget.columnCount()):
                item = QtWidgets.QTableWidgetItem(new_lst[i][j])
                # Make the items non-editable
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.tableWidget.setItem(i, j, item)
# 19approval/disapproval screen
class MedicalApprovalScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pending Approvals Screen')
        self.setGeometry(350, 130, 673, 450)

        # Create the table widget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Doctor Name', 'Medical License#', 'Approve/Deny'])

        # Set the number of rows and populate with random data
        self.tableWidget.setRowCount(5)
        self.populateTableWithData()

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)

        self.backButton = QPushButton('Back', self)
        self.backButton.clicked.connect(self.goBack)

        self.saveButton = QPushButton('Save', self)
        self.saveButton.clicked.connect(self.saveData)

        # Add a horizontal layout for the Save button
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)  # Add stretchable space before the button
        button_layout.addWidget(self.backButton)
        button_layout.addWidget(self.saveButton)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def populateTableWithData(self):
        # You can replace this with your data retrieval logic
        # data = [
        #     ['Dr. Smith', '12345', '555-1234', ''],
        #     ['Dr. Johnson', '67890', '555-5678', ''],
        #     ['Dr. Williams', '13579', '555-9876', ''],
        #     ['Dr. Davis', '24680', '555-4321', ''],
        #     ['Dr. Anderson', '98765', '555-8765', '']
        #  ]
        # After populating the table with data, set the width of the last column
        last_column_index = self.tableWidget.columnCount() - 1
        self.tableWidget.setColumnWidth(last_column_index, 200)
        # After populating the table with data, set the height of all rows
        desired_row_height = 40  # Replace with your preferred height
        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(row, desired_row_height)

        # for row, entry in enumerate(data):
        #     for col, value in enumerate(entry):
        #         item = QTableWidgetItem(str(value))
        #         self.tableWidget.setItem(row, col, item)

        #         # Add radio buttons to the last column
        #         if col == 3:
        #             approve_radio = QRadioButton('Approve')
        #             deny_radio = QRadioButton('Deny')

        #             radio_layout = QHBoxLayout()
        #             radio_layout.addWidget(approve_radio)
        #             radio_layout.addWidget(deny_radio)
        #             radio_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #             widget = QWidget()
        #             widget.setLayout(radio_layout)

        #             self.tableWidget.setCellWidget(row, col, widget)

        #             # Connect the radio buttons to a slot (function)
        #             approve_radio.toggled.connect(lambda state, row=row, col=col: self.radioToggled(state, row, col, 'Approve'))
        #             deny_radio.toggled.connect(lambda state, row=row, col=col: self.radioToggled(state, row, col, 'Deny'))

    def radioToggled(self, state, row, col, value):
        if state:
            print(f'Row {row + 1}, Column {col + 1}: {value} selected')

    def saveData(self):
        # Add logic to save data
        output=QMessageBox(self)              
        output.setWindowTitle("Doctor Approvals") 
        output.setText("Changes saved successfully!.")
        output.setStandardButtons( QMessageBox.StandardButton.Ok)
        output.setIcon(QMessageBox.Icon.Information) 
        button=output.exec()
        print('Data saved!')

    def goBack(self):
        # Add logic to save data
        self.new_form = Admin_homepage("admin")
        self.new_form.show()
        self.close()
        print('back to home page!')

# 20editable patient history view by doctor only
class editable_patient_history(QtWidgets.QMainWindow):  
    def __init__(self):
        super(editable_patient_history, self).__init__() 
        uic.loadUi('edit_patient_record.ui', self) 
        self.setWindowTitle("Patient History")


        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()

        self.save_rec.clicked.connect(self.changes_saved)

        # self.back.clicked.connect(self.go_back_to_app_details)

    def changes_saved(self):
        output=QMessageBox(self)              
        output.setWindowTitle("Patient Medical History") 
        output.setText("Changes saved successfully!.")
        output.setStandardButtons( QMessageBox.StandardButton.Ok)
        output.setIcon(QMessageBox.Icon.Information) 
        button=output.exec()
        self.close()

    # def go_back_to_app_details(self):
    #     self.new_form = Appointments_details()
    #     self.new_form.show()
    #     self.close()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

      
