import pyodbc
import datetime
server = 'DESKTOP-HPUUN98\SPARTA'
database = 'final_ra'  # Name of your Northwind database
use_windows_authentication = True  # Set to True to use Windows Authentication
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

sql_query = """
    INSERT INTO Patient
    ([patient_id],[first_name],[last_name],[email],[password],[DOB],[gender_id],[phone_num],[is_admitted],[emergency_contact])
    VALUES (?,?,?,?,?,?,?,?,?,?)
"""

# Get order information from input fields
patient_id = 1
first_name = "Name" #self.FirstName.text()
last_name = "Last"#self.LastName.text()
email = "Email" #self.email.text()
password = "12345678" #self.password.text()
DOB = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
gender_id = 0
phone_num = "123456788"
is_admitted = 0
emergency_contact = "NULL"

# Execute the SQL query with parameter values
cursor.execute(sql_query, (patient_id,first_name,last_name, email, password, DOB, gender_id, phone_num, is_admitted,emergency_contact))
connection.commit()
connection.close()
