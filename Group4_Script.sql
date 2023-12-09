begin transaction;
CREATE TABLE [patients] (
	patient_id int NOT NULL,
	first_name varchar(38),
	last_name varchar(38),
	email nvarchar(38),
	password nvarchar(38),
	confirm_password nvarchar(38),
	DOB date,
	gender_id int,
	contact numeric(38),
	emergency_contact numeric(38),
	patient_weight int,
  CONSTRAINT [PK_PATIENTS] PRIMARY KEY CLUSTERED
  (
  [patient_id] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [doctor] (
	doctor_id int NOT NULL,
	first_name varchar(38),
	last_name varchar(38),
	email nvarchar(38),
	password nvarchar(38),
	confirm_password nvarchar(38),
	CNIC numeric(38),
	medical_license_num numeric(38),
	assigned_pod nvarchar(38),
	gender_id int,
  CONSTRAINT [PK_DOCTOR] PRIMARY KEY CLUSTERED
  (
  [doctor_id] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [patient_record_diagnosis] (
	appointment_id int NOT NULL,
	diagnosis nvarchar(255),
  CONSTRAINT [PK_PATIENT_RECORD_DIAGNOSIS] PRIMARY KEY CLUSTERED
  (
  appointment_id,diagnosis
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [patient_record_symptoms] (
	appointment_id int NOT NULL,
	symptoms varchar(255),
  CONSTRAINT [PK_PATIENT_RECORD_SYMPTOMS] PRIMARY KEY CLUSTERED
  (
  appointment_id,symptoms 
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [patient_record_allergies] (
	appointment_id int NOT NULL,
	allergies varchar(255),
  CONSTRAINT [PK_PATIENT_RECORD_ALLERGIES] PRIMARY KEY CLUSTERED
  (
  appointment_id,allergies
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [reason_for_visit] (
	appointment_id int NOT NULL,
	reason varchar(255),
  CONSTRAINT [PK_REASON_FOR_VISIT] PRIMARY KEY CLUSTERED
  (
  appointment_id,reason
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO

CREATE TABLE [slots_available] (
	slot_id int NOT NULL,
	doctor_id int,
	year int,
	month int,
	dateday int,
	day varchar(38),
	start_time time,
	end_time time,
	availability_status bit,
  CONSTRAINT [PK_SLOTS_AVAILABLE] PRIMARY KEY CLUSTERED
  (
  [slot_id] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [admin_employee] (
	admin_id int NOT NULL,
	name varchar(38),
	email nvarchar(38),
	password nvarchar(38),
  CONSTRAINT [PK_ADMIN_EMPLOYEE] PRIMARY KEY CLUSTERED
  (
  [admin_id] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [gender] (
	gender_id int NOT NULL,
	gender varchar(38),
  CONSTRAINT [PK_GENDER] PRIMARY KEY CLUSTERED
  (
  [gender_id] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [specialization] (
	specialization_id int NOT NULL,
	specialization varchar(255),
  CONSTRAINT [PK_SPECIALIZATION] PRIMARY KEY CLUSTERED
  (
  [specialization_id] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [doctorspecialization] (
	specialization_id int NOT NULL,
	doctor_id int NOT NULL,
  CONSTRAINT [PK_DOCTORSPECIALIZATION] PRIMARY KEY CLUSTERED
  (
  specialization_id,doctor_id
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [doctorpatient] (
	doctor_id int NOT NULL,
	patient_id int NOT NULL,
  CONSTRAINT [PK_DOCTORPATIENT] PRIMARY KEY CLUSTERED
  (
  doctor_id,patient_id
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [payment_method] (
	payment_method_id int NOT NULL,
	payment_method varchar(38),
  CONSTRAINT [PK_PAYMENT_METHOD] PRIMARY KEY CLUSTERED
  (
  [payment_method_id] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [appointments_booked] (
	appointment_id int NOT NULL,
	slot_id int,
	cancel_appointment bit,
	patient_id int,
	amount money,
	payment_method_id int,
	doctors_advice varchar(1000),
	is_admitted bit,
	room_num int,
	status varchar(38),
	outcome varchar(38),
  CONSTRAINT [PK_PRESCRIPTIONS] PRIMARY KEY CLUSTERED
  (
  [appointment_id] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO

CREATE TABLE [prescriptions] (
	appointment_id int NOT NULL,
	medicine varchar(255),
  CONSTRAINT [PK_APPOINTMENTS_BOOKED] PRIMARY KEY CLUSTERED
  (
  appointment_id,medicine
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO

ALTER TABLE [patients] WITH CHECK ADD CONSTRAINT [patients_fk0] FOREIGN KEY ([gender_id]) REFERENCES [gender]([gender_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [patients] CHECK CONSTRAINT [patients_fk0]
GO

ALTER TABLE [doctor] WITH CHECK ADD CONSTRAINT [doctor_fk0] FOREIGN KEY ([gender_id]) REFERENCES [gender]([gender_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [doctor] CHECK CONSTRAINT [doctor_fk0]
GO

ALTER TABLE [patient_record_diagnosis] WITH CHECK ADD CONSTRAINT [patient_record_diagnosis_fk0] FOREIGN KEY ([appointment_id]) REFERENCES [appointments_booked]([appointment_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [patient_record_diagnosis] CHECK CONSTRAINT [patient_record_diagnosis_fk0]
GO

ALTER TABLE [patient_record_symptoms] WITH CHECK ADD CONSTRAINT [patient_record_symptoms_fk0] FOREIGN KEY ([appointment_id]) REFERENCES [appointments_booked]([appointment_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [patient_record_symptoms] CHECK CONSTRAINT [patient_record_symptoms_fk0]
GO

ALTER TABLE [prescriptions] WITH CHECK ADD CONSTRAINT [prescriptions_fk0] FOREIGN KEY ([appointment_id]) REFERENCES [appointments_booked]([appointment_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [prescriptions] CHECK CONSTRAINT [prescriptions_fk0]
GO

ALTER TABLE [patient_record_allergies] WITH CHECK ADD CONSTRAINT [patient_record_allergies_fk0] FOREIGN KEY ([appointment_id]) REFERENCES [appointments_booked]([appointment_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [patient_record_allergies] CHECK CONSTRAINT [patient_record_allergies_fk0]
GO

ALTER TABLE [reason_for_visit] WITH CHECK ADD CONSTRAINT [reason_for_visit_fk0] FOREIGN KEY ([appointment_id]) REFERENCES [appointments_booked]([appointment_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [reason_for_visit] CHECK CONSTRAINT [reason_for_visit_fk0]
GO

ALTER TABLE [slots_available] WITH CHECK ADD CONSTRAINT [slots_available_fk0] FOREIGN KEY ([doctor_id]) REFERENCES [doctor]([doctor_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [slots_available] CHECK CONSTRAINT [slots_available_fk0]
GO




ALTER TABLE [doctorspecialization] WITH CHECK ADD CONSTRAINT [doctorspecialization_fk0] FOREIGN KEY ([specialization_id]) REFERENCES [specialization]([specialization_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [doctorspecialization] CHECK CONSTRAINT [doctorspecialization_fk0]
GO
ALTER TABLE [doctorspecialization] WITH CHECK ADD CONSTRAINT [doctorspecialization_fk1] FOREIGN KEY ([doctor_id]) REFERENCES [doctor]([doctor_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [doctorspecialization] CHECK CONSTRAINT [doctorspecialization_fk1]
GO

ALTER TABLE [doctorpatient] WITH CHECK ADD CONSTRAINT [doctorpatient_fk0] FOREIGN KEY ([doctor_id]) REFERENCES [doctor]([doctor_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [doctorpatient] CHECK CONSTRAINT [doctorpatient_fk0]
GO
ALTER TABLE [doctorpatient] WITH CHECK ADD CONSTRAINT [doctorpatient_fk1] FOREIGN KEY ([patient_id]) REFERENCES [patients]([patient_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [doctorpatient] CHECK CONSTRAINT [doctorpatient_fk1]
GO


ALTER TABLE [appointments_booked] WITH CHECK ADD CONSTRAINT [appointments_booked_fk0] FOREIGN KEY ([slot_id]) REFERENCES [slots_available]([slot_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [appointments_booked] CHECK CONSTRAINT [appointments_booked_fk0]
GO
ALTER TABLE [appointments_booked] WITH CHECK ADD CONSTRAINT [appointments_booked_fk1] FOREIGN KEY ([patient_id]) REFERENCES [patients]([patient_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [appointments_booked] CHECK CONSTRAINT [appointments_booked_fk1]
GO
ALTER TABLE [appointments_booked] WITH CHECK ADD CONSTRAINT [appointments_booked_fk2] FOREIGN KEY ([payment_method_id]) REFERENCES [payment_method]([payment_method_id])
ON UPDATE NO ACTION
GO
ALTER TABLE [appointments_booked] CHECK CONSTRAINT [appointments_booked_fk2]
GO

commit;