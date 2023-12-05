begin transaction;

--insert into admin , we have three admins at present 
INSERT INTO admin_employee (admin_id,name, email, password)
VALUES
    (1,'Ali Khan', 'ali.khan@example.com', 'P@k1st@n1'),
    (2,'Saima Ahmed', 'saima.ahmed@example.com', 'L@h0r3@2023'),
    (3,'Rizwan Malik', 'rizwan.malik@example.com', 'Kar@ch1@789');
select * from admin_employee
 
-- Insert data into the specialization table
INSERT INTO specialization (specialization_id,specialization)
VALUES
    (1, 'Clinical Psychology'),
    (2, 'Psychiatry'),
    (3, 'Counseling Psychology'),
    (4, 'Neuropsychology'),
    (5, 'Child and Adolescent Psychiatry'),
    (6, 'Health Psychology'),
    (7, 'Mental Health Counseling');
select * from specialization


-- Insert data into the gender table
INSERT INTO gender (gender_id, gender)
VALUES
    (1, 'Male'),
    (2, 'Female'),
    (3, 'Other');
select * from gender

--insert into doctor 
INSERT INTO doctor (doctor_id, first_name, last_name, email, password, confirm_password, CNIC, medical_license_num, assigned_pod, gender_id)
VALUES
    (1, 'Ahmed', 'Khan', 'ahmed.khan@example.com', 'P@ssw0rd', 'P@ssw0rd', 1234512345678, 987654321, 'Room 101', 1),
    (2, 'Saima', 'Malik', 'saima.malik@example.com', 'Secure123', 'Secure123', 2345623456789, 876543210, 'Room 202', 2),
    (3, 'Ali', 'Rizvi', 'ali.rizvi@example.com', 'StrongPwd', 'StrongPwd', 3456734567890, 765432109, 'Room 303', 1),
    (4, 'Farida', 'Hassan', 'farida.hassan@example.com', 'Pass123', 'Pass123', 4567845678901, 654321098, 'Room 404', 2),
    (5, 'Kamran', 'Akhtar', 'kamran.akhtar@example.com', 'SecretPwd', 'SecretPwd', 5678956789012, 543210987, 'Room 505', 1);
select * from doctor

-- Insert data into the doctorspecialization table
INSERT INTO doctorspecialization (specialization_id, doctor_id)
VALUES
    (1, 1),
	(2, 2),
    (3, 3),
    (4, 4), 
    (5, 5),
    (6, 1),
    (7, 3),
    (6, 2);
select * from doctorspecialization

-- Insert data into the patients table
INSERT INTO patients (patient_id, first_name, last_name, email, password, confirm_password, DOB, gender_id, contact, emergency_contact,patient_weight)
VALUES
    (1, 'Ali', 'Ahmed', 'ali.ahmed@example.com', 'P@ssw0rd', 'P@ssw0rd', '1990-05-15', 1, 3001123456, 3456123456,70),
    (2, 'Ayesha', 'Malik', 'ayesha.malik@example.com', 'Secure123', 'Secure123', '1985-08-21', 2, 3002765432, 3456234567, 65),
    (3, 'Imran', 'Shah', 'imran.shah@example.com', 'StrongPwd', 'StrongPwd', '1992-02-10', 1, 3003345678, 3456345678,78),
    (4, 'Saba', 'Riaz', 'saba.riaz@example.com', 'Pass123', 'Pass123', '1988-11-30', 2, 3004456789, 3456456789,60),
    (5, 'Usman', 'Ahmed', 'usman.ahmed@example.com', 'SecretPwd', 'SecretPwd', '1995-07-04', 1, 3005567890, 3456567890,85),
    (6, 'Nida', 'Khan', 'nida.khan@example.com', 'SecurePwd', 'SecurePwd', '1987-04-18', 2, 3006678901, 3456678901,72),
    (7, 'Zainab', 'Ali', 'zainab.ali@example.com', 'Pass@123', 'Pass@123', '1998-09-25', 2, 3007789012, 3456789012,68),
    (8, 'Bilal', 'Khan', 'bilal.khan@example.com', 'Strong@Pwd', 'Strong@Pwd', '1993-03-14', 1, 3008890123, 3457890123,75),
    (9, 'Hina', 'Malik', 'hina.malik@example.com', 'NewPwd@123', 'NewPwd@123', '1989-06-08', 2, 3009001234, 3458901234,92),
    (10, 'Saad', 'Ahmed', 'saad.ahmed@example.com', 'SaadPwd', 'SaadPwd', '1991-12-02', 1, 3000112345, 3450112345,80);
select * from patients

--insert into doctorpatient
INSERT INTO doctorpatient (doctor_id, patient_id)
VALUES
    (1, 1),
    (1, 2), 
    (2, 3),
    (2, 4), 
    (3, 5), 
    (3, 6), 
    (4, 7), 
    (4, 8), 
    (5, 9),
	(3, 1),
    (5, 10); 
select * from doctorpatient

-- Insert data into the payment_method table for multiple payment methods
INSERT INTO payment_method (payment_method_id, payment_method)
VALUES
    (1, 'cash'),
    (2, 'credit card');
select * from payment_method

--insert data into slots_available
-- Additional slots for Doctor 1 (Ahmed Khan)
--insert data into slots_available
-- Additional slots for Doctor 1 (Ahmed Khan)
INSERT INTO slots_available (slot_id, doctor_id,year, month, dateday, day, start_time, end_time, availability_status)
VALUES
    (1, 1,2023,12,4, 'Monday', '09:00 AM', '09:30 AM', 1),
    (2, 1,2023,12,4, 'Monday', '09:30 AM', '10:00 AM', 1),
    (3, 1,2023,12,4, 'Monday', '10:00 AM', '10:30 AM', 1),
    (4, 1,2023,12,4, 'Monday', '10:30 AM', '11:00 AM', 1),
    (5, 1,2023,12,6, 'Wednesday', '04:00 PM', '04:30 PM', 1),
    (6, 1,2023,12,6, 'Wednesday', '04:30 PM', '05:00 PM', 0), -- No availability
    (7, 1,2023,12,6, 'Wednesday', '05:00 PM', '05:30 PM', 1),
    (8, 1, 2023,12,6,'Wednesday', '05:30 PM', '06:00 PM', 1);

-- Additional slots for Doctor 2 (Saima Malik)
INSERT INTO slots_available (slot_id, doctor_id, year, month, dateday,day, start_time, end_time, availability_status)
VALUES
    (9, 2,2023,12,5, 'Tuesday', '10:00 AM', '10:30 AM', 1),
    (10, 2,2023,12,5, 'Tuesday', '10:30 AM', '11:00 AM', 1),
    (11, 2, 2023,12,5, 'Tuesday', '11:00 AM', '11:30 AM', 1),
    (12, 2, 2023,12,5, 'Tuesday', '11:30 AM', '12:00 PM', 1),
    (13, 2,2023,12,7, 'Thursday', '02:00 PM', '02:30 PM', 1),
    (14, 2,2023,12,7, 'Thursday', '02:30 PM', '03:00 PM', 1),
    (15, 2,2023,12,7, 'Thursday', '03:00 PM', '03:30 PM', 0), -- No availability
    (16, 2, 2023,12,7,'Thursday', '03:30 PM', '04:00 PM', 1);

-- Additional slots for Doctor 3 (Ali Rizvi)
INSERT INTO slots_available (slot_id, doctor_id,year, month, dateday, day, start_time, end_time, availability_status)
VALUES
    (17, 3,2023,12,4, 'Monday', '01:00 PM', '01:30 PM', 1),
    (18, 3,2023,12,4, 'Monday', '01:30 PM', '02:00 PM', 1),
    (19, 3,2023,12,4, 'Monday', '02:00 PM', '02:30 PM', 1),
    (20, 3,2023,12,4, 'Monday', '02:30 PM', '03:00 PM', 1),
    (21, 3,2023,12,8, 'Friday', '09:00 AM', '09:30 AM', 1),
    (22, 3,2023,12,8, 'Friday', '09:30 AM', '10:00 AM', 1),
    (23, 3,2023,12,8, 'Friday', '10:00 AM', '10:30 AM', 1),
    (24, 3,2023,12,8, 'Friday', '10:30 AM', '11:00 AM', 1);
-- Additional slots for Doctor 4 (Farida Hassan) with 1.5-hour duration
INSERT INTO slots_available (slot_id, doctor_id,year, month, dateday, day, start_time, end_time, availability_status)
VALUES
    (25, 4, 2023,12,5,'Tuesday', '02:00 PM', '02:30 PM', 1), -- 1st half-hour slot
    (26, 4,2023,12,5, 'Tuesday', '02:30 PM', '03:00 PM', 1), -- 2nd half-hour slot
    (27, 4,2023,12,5, 'Tuesday', '03:00 PM', '03:30 PM', 1); -- 3rd half-hour slot

-- Additional slots for Doctor 5 (Kamran Akhtar) with 1.5-hour duration
INSERT INTO slots_available (slot_id, doctor_id,year, month, dateday, day, start_time, end_time, availability_status)
VALUES
    (28, 5, 2023,12,6,'Wednesday', '09:00 AM', '09:30 AM', 1), -- 1st half-hour slot
    (29, 5,2023,12,6, 'Wednesday', '09:30 AM', '10:00 AM', 1), -- 2nd half-hour slot
    (30, 5,2023,12,6, 'Wednesday', '10:00 AM', '10:30 AM', 1); -- 3rd half-hour slot
select * from slots_available 

-- Insert data into the appointments_booked table with realistic mental health medication
INSERT INTO appointments_booked (appointment_id, slot_id, cancel_appointment, patient_id, amount, payment_method_id, doctors_advice, is_admitted, room_num, status, outcome)
VALUES
    (1, 1, 0, 1, 700.00, 1, 'Take 50mg of Sertraline once daily in the morning for depression', 1, 12, 'Condition Worsened', NULL),
    (2, 9, 0, 2, 700.00, 2, 'Take 0.5mg of Lorazepam as needed for acute anxiety symptoms, not exceeding three times a day', 0, NULL, 'Significant Improvement', 'Discharged'),
    (3, 17, 0, 3, 700.00, 1, 'Start Fluoxetine with 20mg once daily in the morning, and we will assess progress during the next appointment', 0, NULL, 'Mild Improvement', 'Discharged'),
    (4, 25, 0, 4, 700.00, 2,  'Continue Bupropion with 150mg once daily in the morning for managing depressive symptoms', 0, NULL, 'Moderate Improvement', 'Lost for follow-Up'),
    (5, 28, 0, 5, 700.00, 1,  'Maintain Escitalopram at 10mg once daily in the evening for mood stability', 0, NULL, 'No Change', 'Transfer'),
    (6, 12, 1, 6, 700.00, 2, 'Start Quetiapine with 25mg at bedtime and we will review its impact during the next session', 0, NULL, 'Condition Worsened', 'Death'),
    (7, 20, 0, 7, 700.00, 1,  'Consider Venlafaxine at 75mg once daily in the morning to address depressive symptoms, and we will discuss any adjustments in our follow-up', 1, 10, 'Condition Worsened', NULL),
    (8, 20, 0, 7, 700.00, 1,  'Exercise daily in the morning to address depressive symptoms, and we will discuss any adjustments in our follow-up', 0, NULL, NULL, NULL);
select * from appointments_booked

--inserting into patientrecordsymptoms 
INSERT INTO patient_record_symptoms (appointment_id, symptoms)
VALUES
	(1, 'Persistent low mood'),
	(1, 'feelings of sadness'),
	(1, 'trouble sleeping'),
	(1, 'increased stress levels'),
	(1, 'Difficulty concentrating'),
	(2, 'difficulty falling '),
	(2, 'Persistent anxiety'),
	(2, 'poor sleep patterns'),
	(3, 'Worsened mood'),
	(3, 'increased depressive symptoms'),
	(4, 'low energy levels'),
	(4, 'Unstable mood'),
	(5, 'Mood instability'),
	(5, 'heightened irritability'),
	(6, 'Frequent mood swings'),
	(6, 'emotional distress'),
	(7, 'Persistent low mood'),
	(7, 'reduced interest'),
	(7, 'fatigue');
select * from [patient_record_symptoms]

--inserting in reason for visit
INSERT INTO reason_for_visit (appointment_id, reason)
VALUES
    (1, 'Counselling'),
    (2, 'Psychotherapy'),
    (3, 'Regular sessions'),
    (4, 'Follow-up appointment'),
	(4, 'Regular sessions'),
    (5, 'Therapeutic consultation'),
	(5, 'Counselling'),
    (6, 'Emotional well-being check'),
	(6, 'Regular sessions'),
    (7, 'Mental health assessment');
select * from reason_for_visit


--insert into alleergies
INSERT INTO patient_record_allergies (appointment_id, allergies)
VALUES
    (1, 'None'),
    (2, 'None'),
    (3, 'Pollen'),
    (3, 'Dust'),
    (4, 'Erythromycin'),
    (5, 'None'),
    (6, 'None'),
    (7, 'Penicillin'),
    (7, 'Aspirin');
select * from patient_record_allergies

-- Insert data into the patient_record_diagnosis table with diagnoses for appointment 1
INSERT INTO patient_record_diagnosis (appointment_id, diagnosis)
VALUES
    (1, 'Mild depression'),
    (1, 'Adjustment disorder'),
    (1, 'Work-related stress'),
    (2, 'Generalized anxiety disorder'),
    (2, 'Sleep disorder'),
    (3, 'Seasonal affective disorder (SAD)'),
    (4, 'Depressive disorder'),
    (5, 'Stable mood with Escitalopram'),
    (6, 'Bipolar disorder'),
    (6, 'Anxiety disorder'),
    (7, 'Depressive disorder');
select * from patient_record_diagnosis

-- Insert data into the prescriptions table with medications for appointment 1
INSERT INTO prescriptions(appointment_id, medicine)
VALUES
    (1, 'Fluoxetine'),
    (1, 'Bupropion'),
    (2, 'Lorazepam'),
    (3, 'Escitalopram'),
    (4, 'Bupropion'),
    (5, 'Escitalopram'),
    (6, 'Quetiapine'),
    (7, 'Prescription-free sleep aids');
select * from prescriptions


commit;



