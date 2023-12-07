from PyQt6 import QtWidgets, uic, QtGui, QtCore
from PyQt6.QtWidgets import QDialog, QApplication, QWidget,  QGridLayout, QListWidget,  QPushButton, QMainWindow, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QRadioButton, QHBoxLayout, QHeaderView
import sys 
from datetime import date
import pyodbc
from PyQt6.QtCore import Qt


server = 'DESKTOP-2TB3VB3\SPARTA'
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
                    self.new_form = Doctor_homepage("doctor",login_email)
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
                    self.new_form = Admin_homepage("admin",login_email) 
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
            output.setText("Successfully Signed Up!")
            output.setStandardButtons( QMessageBox.StandardButton.Ok)
            output.setIcon(QMessageBox.Icon.Information) 
            button=output.exec()
            self.new_form = ViewBook3()
            self.new_form.show()
            self.close()


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
    def __init__(self,user,login_email):
        super(Admin_homepage, self).__init__() 
        uic.loadUi('adminhomepage.ui', self) 
        self.setWindowTitle("Admin Homepage")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        print(user)
        self.show()
        self.login_email = login_email

        self.logout_admin.clicked.connect(self.admin_logout)

        self.patient_admin.clicked.connect(self.admin_patient_view)

        self.doc_admin.clicked.connect(self.admin_doc_view)
    
        self.payments.clicked.connect(self.view_payments)


    def admin_logout(self):
        self.new_form = ViewBook3()
        self.new_form.show()
        self.close()

    def admin_doc_view(self):
        self.new_form = doctors_list(self.login_email)
        self.new_form.show()
        self.close()

    def admin_patient_view(self):
        self.new_form = Patient_Records("admin", self.login_email)
        self.new_form.show()
        self.close()

    def view_payments(self):
        self.new_form = payment_details(self.login_email)
        self.new_form.show()
        self.close()

# 7doctor homepage
class Doctor_homepage(QtWidgets.QMainWindow):  
    def __init__(self,user,login_email):
        super(Doctor_homepage, self).__init__() 
        uic.loadUi('dochomepage.ui', self) 
        self.setWindowTitle("Doctor Homepage")
        
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()
        
        self.login_email = login_email
        
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        
        cursor = connection.cursor()
        cursor.execute("""
                    SELECT 
                    doctor_id
                FROM doctor where email = ?;
                """, login_email)
        self.doctorID = cursor.fetchall()[0][0]

        self.logout_doctor.clicked.connect(self.patient_logout)

        self.patients.clicked.connect(self.patient_details)

        self.app.clicked.connect(self.appointment_list)
        

    def patient_logout(self):
        self.new_form = ViewBook3()
        self.new_form.show()
        self.close()

    def appointment_list(self):
        self.new_form = Appointments(self.doctorID,self.login_email)
        self.new_form.show()
        self.close()

    def patient_details(self):
        self.new_form = Patient_Records("doctor",self.login_email)
        self.new_form.show()
        self.close()

# 8patient homepage
class Patient_homepage(QtWidgets.QMainWindow):  
    def __init__(self, email="default"):
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

        self.view_booked_app.clicked.connect(self.my_appointments)

    def patient_logout(self):
        self.new_form = ViewBook3()
        self.new_form.show()
        self.close()

    def private_records(self):
        self.new_form = Private_view_patient(self.email)
        self.new_form.show()
        self.close()
    
    def book_appointment(self):
        self.new_form = Appointments_booking(self.email)
        self.new_form.show()
        self.close()

    def my_appointments(self):
        self.new_form = patient_booked_appointments(self.email)
        self.new_form.show()
        self.close()


# 9patient list
class Patient_Records(QtWidgets.QMainWindow):  
    def __init__(self,user,login_email):
        super(Patient_Records, self).__init__() 
        uic.loadUi('patient_records.ui', self) 
        self.setWindowTitle("Patient List")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()
        self.user = user
        self.login_email = login_email
        # print(self.user)
        
        self.search_patient.clicked.connect(self.search_pat)

        self.back_button.clicked.connect(self.back_to_dochome)

        self.view_button.clicked.connect(self.patient_history)

        self.populate_table()

    def back_to_dochome(self):
        if self.user == 'admin':
            print('line460')
            self.new_form1 = Admin_homepage("admin",self.login_email) 
            self.new_form1.show()
      
        elif self.user == 'doctor':
            self.new_form2 = Doctor_homepage("doctor",self.login_email)
            self.new_form2.show()
      
        self.close()

    def patient_history(self):
        chosen_row = self.tableWidget.currentRow()
        
        if chosen_row != -1:
            firstname= self.tableWidget.item(chosen_row,0).text()
            p_contact = self.tableWidget.item(chosen_row,4).text()
            # print(firstname,p_contact)
            
            
        self.new_form = Patient_History(self.user,firstname,p_contact)
        self.new_form.show()
        self.close()

    def search_pat(self):
        inputname = self.patient_name.text().lower()

        # Create a SQL query to search for patients based on the input name
        query = f"""
            SELECT 
                first_name+' '+last_name,
                year(GETDATE()) - year(DOB) as age,
                (SELECT TOP 1 gender FROM gender WHERE patients.gender_id = gender.gender_id) AS gender,
                DOB,
                contact
            FROM patients
            WHERE first_name LIKE ? OR last_name LIKE ?;
        """

        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()
        cursor.execute(query, ('%' + inputname + '%', '%' + inputname + '%'))

        # Clear the table before populating with new data
        self.tableWidget.clear()

        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.tableWidget.setItem(row_index, col_index, item)

    # Close the database connection
        connection.close()


    def populate_table(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        
        cursor = connection.cursor()
        cursor.execute("""
                    SELECT 
                    first_name+' '+last_name,
                    year(GETDATE()) - year(DOB) as age,
                    (SELECT TOP 1 gender FROM gender WHERE patients.gender_id = gender.gender_id) AS gender,
                    DOB,
                    contact
                FROM patients;

                """)
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
        
        # Create the connection string based on the authentication method chosen
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        # TODO: Write SQL query to fetch orders data
        cursor.execute("""
                    select patient_id from patients where first_name+' '+last_name = ? and contact = ?

                """,firstname,p_contact)
        
        patientID = cursor.fetchone()[0]
        
        self.populate_screen(patientID)
        
        # self.checkBox_6.clear()

    def back_to_list(self):
        self.new_form = Patient_Records(self.user)
        self.new_form.show()
        self.close()
        
    def populate_screen(self,patientID):
        # Create the connection string based on the authentication method chosen
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        # TODO: Write SQL query to fetch orders data
        cursor.execute("""
                    select first_name,last_name,email,DOB,contact,emergency_contact,year(GETDATE()) - year(DOB) as age,gender,patient_weight from patients join gender on patients.gender_id=gender.gender_id where patient_id = ?

                """,patientID)
        
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

            
        # else:
            # print('no')
        
        # patientid = patient_info[0][-1]

        cursor.execute("""
            SELECT P.patient_id, A.appointment_id, COUNT(P.patient_id) as visitNumbers
            FROM Patients P
            JOIN Appointments_booked A ON P.patient_id = A.patient_id
            WHERE P.patient_id = ?
            GROUP BY P.patient_id, A.appointment_id;
        """, patientID)

        patient_appointments = cursor.fetchall()
        # print(patient_appointments)
        
        
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
        # print(f"Selected Text: {selected_text}")
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
        # print(admitted)
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
    def __init__(self,doctorID,login_email):
        super(Appointments, self).__init__() 
        uic.loadUi('updated_appointments.ui', self) 
        self.setWindowTitle("Appointments List")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()
        
        self.doctorID = doctorID
        self.login_email = login_email
        
        self.search_app.clicked.connect(self.search_appointments)
        self.back_to_doc_home.clicked.connect(self.backtohome)

        self.view_app_details.clicked.connect(self.appointment_expanded)
        self.populate_appointment_table()

    def appointment_expanded(self):
        chosen_row = self.apptable.currentRow()
        
        if chosen_row != -1:
            
            name = self.apptable.item(chosen_row, 0).text()
            doctor = self.apptable.item(chosen_row, 1).text()
            # contact = cursor.fetchall()
            time = self.apptable.item(chosen_row, 2).text()
            day = self.apptable.item(chosen_row, 3).text()
            cancelled=eval(self.apptable.item(chosen_row, 4).text())
            # print(name,time,day,cancelled)

        self.new_form = Appointments_details(name, time, day, cancelled,doctor)
        self.new_form.show()
        self.close()

    def backtohome(self):
        self.new_form = Doctor_homepage("doctor",self.login_email)
        self.new_form.show()
        self.close()
        
    def search_appointments(self):
        name_input = self.patient_app.text().lower()

        # Create a SQL query to search for appointments based on patient names
        query = """
            SELECT 
                p.first_name + ' ' + p.last_name AS patient_name,
                d.first_name + ' ' + d.last_name AS doctor_name,
                s.start_time as appointment_start_time,
                s.day as appointment_day,
                a.cancel_appointment as appointment_cancel_status
            FROM patients p
            JOIN appointments_booked a ON p.patient_id = a.patient_id
            JOIN slots_available s ON s.slot_id = a.slot_id
            JOIN doctor d ON d.doctor_id = s.doctor_id
            WHERE p.first_name LIKE ? OR p.last_name LIKE ?;
        """

        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()
        cursor.execute(query, ('%' + name_input + '%', '%' + name_input + '%'))

        # Clear the table before populating with new data
        self.apptable.clear()

        for row_index, row_data in enumerate(cursor.fetchall()):
            self.apptable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(cell_data))
                # Make the items non-editable
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.apptable.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

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
    def __init__(self, name, time, day, cancelled,doctor):
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
        
        self.doctor = doctor

        self.back_to_app_list.clicked.connect(self.back_to_applist)
        
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()

        
        cursor.execute("""
            SELECT patient_id
            FROM patients
            WHERE first_name + ' ' + last_name = ?;
        """, name)
        
        patientID = cursor.fetchone()[0]
        self.patientID = patientID
        # print(patientID)
        self.insert_contact(patientID)
        
        cursor.execute("""
            SELECT doctor_id
            FROM doctor
            WHERE first_name +' '+last_name = ?;
        """, doctor)
        
        doctorID = cursor.fetchall()[0][0]
        
        cursor.execute("""
            SELECT slot_id
            FROM slots_available
            WHERE doctor_id = ? and day = ? and start_time = ?;
        """, doctorID,day,time)
        
        slotID = cursor.fetchall()[0][0]
        print(slotID)
        self.slotID = slotID
        
        self.edit_history.clicked.connect(self.patient_his_editable)
        
        # self.search_appointment_and_update_date(name)
        
        connection.close()
        
        
    def insert_contact(self,patientID):
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
            connection = pyodbc.connect(connection_string)

            cursor = connection.cursor()

            
            cursor.execute("""
                SELECT contact
                FROM patients
                WHERE patient_id = ?;
            """, patientID)

            contact_info = cursor.fetchall()

            if contact_info:
                # Fetch the contact information from the result
                contact_value = contact_info[0][0]

                # Clear existing text in the line edit (assuming self.lineEditContact is your line edit widget)
                self.lineEdit_2.clear()

                # Set the contact information in the line edit
                self.lineEdit_2.setText(str(contact_value))

            else:
                # Handle the case where no contact information is found
                self.lineEdit_2.clear()
                # Optionally, display a message or take other appropriate actions

            connection.close()  # Make sure to close the connection even if an exception occurs

        
    def back_to_applist(self):
        self.new_form = Appointments()
        self.new_form.show()
        self.close()

    def patient_his_editable(self):
        self.new_form = editable_patient_history(self.patientID,self.slotID)
        self.new_form.show()
        
# 13slots available booking
class Appointments_booking(QtWidgets.QMainWindow):  
    def __init__(self,login_email):
        super(Appointments_booking, self).__init__() 
        uic.loadUi('patientappointment.ui', self) 
        self.setWindowTitle("Slots Available")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.show()

        self.back_to_booking.clicked.connect(self.backtobooking)

        self.booking_done.clicked.connect(self.app_booked)
        self.login_email=login_email
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
        self.new_form = Patient_homepage()
        self.new_form.show()
        self.close()

    def app_booked(self):
        output=QMessageBox(self)              
        output.setWindowTitle("Appointment") 
        output.setText("Your appointment has been successfully booked!.")
        self.insert_appointment_details(self.login_email)
        output.setStandardButtons( QMessageBox.StandardButton.Ok)
        output.setIcon(QMessageBox.Icon.Information) 
        button=output.exec()
        self.new_form = Patient_homepage()
        self.new_form.show()
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
    def insert_appointment_details(self,login_email):
        
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        #print(appointment_id, slot_id, cancel_appointment, patient_id, amount, payment_method_id, doctors_advice, is_admitted, room_num, status, outcome)
     

        sql_query = """
            INSERT INTO appointments_booked
            ([appointment_id], [slot_id], [cancel_appointment], [patient_id], [amount], [payment_method_id], [doctors_advice], [is_admitted],[room_num], [status],[outcome])
            VALUES (?,?,?,?,?,?,?,?,?,?,?)
        """

        cursor.execute("""SELECT MAX(appointment_id) AS appointment_id FROM appointments_booked""")
        result = cursor.fetchone()
        appointment_id = result[0] + 1

        year = self.comboBox_2.currentText()
        month = self.comboBox_4.currentText()
        dateday = self.comboBox_5.currentText()
        time = self.comboBox_3.currentText().split('-')[0]

        cursor.execute("""
            SELECT slot_id
            FROM slots_available
            WHERE year = ? AND month = ? AND dateday = ? AND start_time = ?
        """, year, month, dateday, time)

        slot_id = cursor.fetchone()[0]  # Fetch the first column of the result

        cancel_appointment = 0
        
        cursor.execute(
        """select patient_id from patients where email = ?
        """, self.login_email
        )
        patient_id = cursor.fetchone()[0]
        amount = 700
        payment_method_id = 2
        doctors_advice = ''
        is_admitted = 0
        room_num = 0
        status =''
        outcome = ''
        print(appointment_id, slot_id, cancel_appointment, patient_id, amount, payment_method_id, doctors_advice, is_admitted, room_num, status, outcome)
        cursor.execute(sql_query, int(appointment_id), int(slot_id), cancel_appointment, int(patient_id), amount, int(payment_method_id), doctors_advice, is_admitted, int(room_num), status, outcome)
        connection.commit()
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
                    select patient_id from patients join gender on patients.gender_id=gender.gender_id where email =?

                """,email)  #all emails are unique in our database
        
        patientID = cursor.fetchone()[0]
        # print(patientID)
        
        cursor.execute("""
                    select first_name,last_name,email,DOB,contact,emergency_contact,year(GETDATE()) - year(DOB) as age,gender,patient_weight from patients join gender on patients.gender_id=gender.gender_id where patient_id =?

                """,patientID)  #all emails are unique in our database
        
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
        # patientid = patient_info[0][-1]

        cursor.execute("""
            SELECT P.patient_id, A.appointment_id, COUNT(P.patient_id) as visitNumbers
            FROM Patients P
            JOIN Appointments_booked A ON P.patient_id = A.patient_id
            WHERE P.patient_id = ?
            GROUP BY P.patient_id, A.appointment_id;
        """, patientID)

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
    def __init__(self, login_email):
        super(doctors_list, self).__init__() 
        uic.loadUi('Doctors_list.ui', self) 
        self.setWindowTitle("Doctors List")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        self.login_email = login_email

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
        self.new_form = Admin_homepage('admin', self.login_email)
        self.new_form.show()
        self.close()

    def search_doctor(self):
        current_specialization = self.comboBox.currentText().lower()

        # Create a SQL query to search for doctors based on specialization
        query = """
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
                specialization s ON ds.specialization_id = s.specialization_id
            WHERE s.specialization = ?;
        """

        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()
        cursor.execute(query, (current_specialization,))

        # Clear the table before populating with new data
        self.tableWidget.clear()

        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.tableWidget.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()


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
    def __init__(self, login_email):
        super(payment_details, self).__init__() 
        uic.loadUi('payment_admin.ui', self) 
        self.setWindowTitle("Payment Details Page")

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
        self.show()
        self.login_email = login_email

        self.search_payment.clicked.connect(self.search_pay)

        self.back_to_adminpage.clicked.connect(self.back_to_adminhome)
        
        self.populate_table()

    def back_to_adminhome(self):
        self.new_form = Admin_homepage("admin", self.login_email)
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

        # Create a SQL query to search for payments based on the patient name
        query = """
            SELECT 
                patients.first_name + ' ' + patients.last_name as patient_name,
                appointments_booked.amount,
                payment_method.payment_method,
                slots_available.start_time,
                slots_available.end_time
            FROM appointments_booked
            JOIN patients ON appointments_booked.patient_id = patients.patient_id
            JOIN payment_method ON appointments_booked.payment_method_id = payment_method.payment_method_id
            JOIN slots_available ON slots_available.slot_id = appointments_booked.slot_id
            WHERE patients.first_name LIKE ? OR patients.last_name LIKE ?;
        """

        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()
        cursor.execute(query, ('%' + name_input + '%', '%' + name_input + '%'))

        # Clear the table before populating with new data
        self.tableWidget.clear()

        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(cell_data))
                # Make the items non-editable
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.tableWidget.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

# 19patient can view their own appointments
class patient_booked_appointments(QtWidgets.QMainWindow):
    def __init__(self, email):
        super(patient_booked_appointments, self).__init__() 
        uic.loadUi('app_booked(patient).ui', self) 
        # ... (other initialization code)

        self.show()
        self.email = email
        
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        
        # Fetch patient ID
        cursor.execute("""select patient_id from patients where email = ?""", self.email)
        result = cursor.fetchall()

        if result:
            patientID = result[0][0]
            self.populate_doctor_appointment_table(patientID)
        else:
            # Handle the case where no patient ID is found for the given email
            print("Patient ID not found for email:", self.email)

        self.pushButton.clicked.connect(self.backtohomepage)

        self.populate_doctor_appointment_table(patientID)

    def backtohomepage(self):
        self.new_form = Patient_homepage()
        self.new_form.show()
        self.close()

    def populate_doctor_appointment_table(self,patientID):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        
        self.patientID = patientID
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        
        # TODO: Write SQL query to fetch doctor appointment data with assigned pod
        cursor.execute("""
                    SELECT 
                        d.first_name + ' ' + d.last_name AS doctor_name,
                        d.assigned_pod AS doctor_assigned_pod,
                        s.day AS appointment_day,
                        FORMAT(CONVERT(datetime, s.year + '-' + s.month + '-' + s.dateday), 'dd/MM/yyyy') AS appointment_date, 
                       CONVERT(VARCHAR, s.start_time, 108) AS appointment_start_time
                    FROM appointments_booked a
                    JOIN slots_available s ON a.slot_id = s.slot_id
                    JOIN doctor d ON d.doctor_id = s.doctor_id where patient_id = ?;
                """,self.patientID)


        for row_index, row_data in enumerate(cursor.fetchall()):
            self.doctor_appointment_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.doctor_appointment_table.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust content display
        header = self.doctor_appointment_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)

# 20editable patient history view by doctor only
class editable_patient_history(QtWidgets.QMainWindow):  
    def __init__(self,patientID,slotID):
        super(editable_patient_history, self).__init__() 
        uic.loadUi('edit_patient_record.ui', self) 
        self.setWindowTitle("Patient History")
        
        # print(patientID)
        self.patientID = patientID
        self.slotID = slotID
        self.appoint_ids = []

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        self.populate_screen(self.patientID)
        
        self.show()
        

        self.addButton.clicked.connect(self.add_symptoms)
        
        self.addButton2.clicked.connect(self.add_diagnosis)
        
        self.addButton3.clicked.connect(self.add_allergies)
        
        self.addButton4.clicked.connect(self.add_treatment)
        
        self.save_rec.clicked.connect(self.changes_saved)
        
    def add_symptoms(self):
        symptoms = self.lineEdit_13.text()
        self.listWidget.addItem(symptoms)
        self.lineEdit_13.clear()
        
    def add_diagnosis(self):
        diagnosis = self.lineEdit_17.text()
        self.listWidget_3.addItem(diagnosis)
        self.lineEdit_17.clear()
        
    def add_allergies(self):
        allergies = self.lineEdit_7.text()
        self.listWidget_2.addItem(allergies)
        self.lineEdit_7.clear()
        
    def add_treatment(self):
        treatment = self.lineEdit.text()
        self.listWidget_4.addItem(treatment)
        self.lineEdit.clear()
    
    def changes_saved(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()
        
        cursor.execute("""
            SELECT count(appointment_id) from appointments_booked
            """)
        
        current_appointment = cursor.fetchall()[0][0]+1
        # print("app = ", current_appointment)
        
        if self.listWidget_4.item(0) is not None:
            doctorAdvice = self.listWidget_4.item(0).text()
            # print("advice = ",doctorAdvice)
        else:
            doctorAdvice = 'none'
        if self.checkBox_6.isChecked():
            admitted = 1
            room = self.lineEdit_10.text()
            # print("room = ", room)
        else:
            admitted = 0
            room = 0
        
        if self.radioButton_9.isChecked():
            status = 'Discharged'
        elif self.radioButton_10.isChecked():
            status = 'Lost for follow-Up'
        elif self.radioButton_11.isChecked():
            status = 'Transfer'
        elif self.radioButton_8.isChecked():
            status = 'Death'
        else:
            status = 'NULL'
            
        if self.radioButton_2.isChecked():
            outcome = 'Significant Improvement'
        elif self.radioButton_3.isChecked():
            outcome = 'Moderate Improvement'
        elif self.radioButton_4.isChecked():
            outcome = 'Mild Improvement'
        elif self.radioButton_5.isChecked():
            outcome = 'No Change'
        elif self.radioButton_6.isChecked():
            outcome = 'Condition Worsened'
        else:
            outcome = 'NULL'
        
        cursor.execute("""
            INSERT INTO appointments_booked (appointment_id, slot_id, cancel_appointment, patient_id, amount, doctors_advice, is_admitted, room_num, status, outcome)
            VALUES
            (?, ?,0,?,700.00,?,?,?,?,?)
            """,current_appointment,self.slotID,self.patientID,doctorAdvice,admitted,room,status,outcome)
        
        
        # storing symptoms from list widget
        for i in range(self.listWidget.count()):
            symptom = self.listWidget.item(i).text()
            # print(symptom)
            cursor.execute("""
            INSERT INTO patient_record_symptoms (appointment_id, symptoms)
            VALUES
            (?, ?)
            """,current_appointment,symptom)
            
        for i in range(self.listWidget_3.count()):
            diagnosis = self.listWidget_3.item(i).text()
            # print(diagnosis)
            cursor.execute("""
            INSERT INTO patient_record_diagnosis (appointment_id, diagnosis)
            VALUES
            (?, ?)
            """,current_appointment,diagnosis)
            
        for i in range(self.listWidget_2.count()):
            allergies = self.listWidget_2.item(i).text()
            # print(allergies)
            cursor.execute("""
            INSERT INTO patient_record_allergies (appointment_id, allergies)
            VALUES
            (?, ?)
            """,current_appointment,allergies)
            
        for i in range(1,self.listWidget_4.count()+1):
            if self.listWidget_4.item(i) is not None:
                medicines = self.listWidget_4.item(i).text()
                # print(medicines)
                cursor.execute("""
                INSERT INTO prescriptions (appointment_id, medicine)
                VALUES
                (?, ?)
                """,current_appointment,medicines)
            
        if self.checkBox.isChecked():
            reason = 'Counseling'
            cursor.execute("""
            INSERT INTO reason_for_visit (appointment_id, reason)
            VALUES
            (?, ?)
            """,current_appointment,reason)
        if self.checkBox_4.isChecked():
            reason = 'Psychotheraphy'
            cursor.execute("""
            INSERT INTO reason_for_visit (appointment_id, reason)
            VALUES
            (?, ?)
            """,current_appointment,reason)
        if self.checkBox_5.isChecked():
            reason = 'Regular Sessions'
            cursor.execute("""
            INSERT INTO reason_for_visit (appointment_id, reason)
            VALUES
            (?, ?)
            """,current_appointment,reason)
        if self.lineEdit_19.text():
            reason = self.lineEdit_19.text()
            cursor.execute("""
            INSERT INTO reason_for_visit (appointment_id, reason)
            VALUES
            (?, ?)
            """,current_appointment,reason)
            
            
        connection.commit()
        connection.close()
        
        
        
        output=QMessageBox(self)              
        output.setWindowTitle("Patient Medical History") 
        output.setText("Changes saved successfully!.")
        output.setStandardButtons( QMessageBox.StandardButton.Ok)
        output.setIcon(QMessageBox.Icon.Information) 
        button=output.exec()
        self.close()
        
    def populate_screen(self,patientID):
        self.patientID = patientID
        # Create the connection string based on the authentication method chosen
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)
        
        # Create a cursor to interact with the database
        cursor = connection.cursor()
        # TODO: Write SQL query to fetch orders data
        cursor.execute("""
                    select first_name,last_name,email,DOB,contact,emergency_contact,year(GETDATE()) - year(DOB) as age,gender,patient_weight from patients join gender on patients.gender_id=gender.gender_id where patient_id = ?

                """,patientID)
        
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
            
        cursor.execute("""
            SELECT P.patient_id, COUNT(P.patient_id) as visitNumbers
            FROM Patients P
            JOIN Appointments_booked A ON P.patient_id = A.patient_id
            WHERE P.patient_id = ?
            GROUP BY P.patient_id
        """, patientID)

        current_visit_no = cursor.fetchall()[0][1]+1
        self.lineEdit_8.setText(str(current_visit_no))
                
        # Close the database connection
        connection.close()
        


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

      
