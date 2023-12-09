Mental Health Database Management System 

Project Overview: 

The Mental Health Database Management System is a project initiated to address the challenges faced by mental health organizations in Pakistan, particularly in Karachi. The inspiration behind this project stems from the reliance on outdated, physical file-based data systems in government sectors, leading to inefficiencies in data management. 

In response to the pressing mental health issues in Pakistan and the inadequate resources available, our project aims to develop a comprehensive database management system tailored for residents of Karachi. The system facilitates the connection between users (patients and doctors), provides access to medical history, tracks progress, and offers functionalities such as payments and admin oversight. 

Scope: 

The project's scope is considered low to medium-scale, focusing on gathering and managing data from Karachi, the largest city in Pakistan. 

Prerequisites: 

Before running the application, ensure you have the following prerequisites installed: 

1. Microsoft SQL Server 

2. Visual Studio Code 

3. Python 

4. PyQt6 

5. Qt Designer 

Installation: 

1. Unzip the provided folder Group4_Project: Extract All -> Extract. 

Database Setup: 

2. Open MS SQL Server. Database -> New Database. Name it whatever you like, say Group4_ProjectDatabase. 

3. Select the newly created database. Open the provided SQL Script named Group4_Script. 

4. Execute the script. It should execute successfully without any errors. 

5. Open the provided SQL Script for data insertion queries named Group4_Insertion. 

6. Execute this script as well. This will insert all the dummy data into the database. 

Running the Application: 

7. Launch VS Code. 

8. Open the extracted folder Group4_project. 

9. Open the patient.py file. 

10. On line number 9 of the file, change the part DESKTOP-2TB3VB3 of the server to your SQL Server. 

server = 'DESKTOP-2TB3VB3\SPARTA' 

11. On line number 10 of the file, change the part Group4_ProjectDatabase of the database to your named database above (which was of example Group4_ProjectDatabase) 

database = 'Group4_ProjectDatabase' 

12. Click on the Run triangular button. Or Run-> Run Without Debugging. Alternatively, you can press Ctrl+F5 to run the program. 

User Guide: 

1. The application provides functionalities for users to connect with relevant professionals, retrieve medical history, and track progress. 

2. The usage is pretty simple. Login/ Signup from whatever user you want and explore! 