import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Patient, Doctor, Appointment

DATABASE_URL = "sqlite:///schedualy.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Initializing the database
def init_db():
    Base.metadata.create_all(engine)
    print("Database initialized")

#-------------- PATIENTS DATABASE ---------------------
def create_patient():
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    illness = input("Patient's illness: ")
    phone = input("Telephone Number: ")
    email = input("Patient's email address: ")

    patient = Patient(name=name, age=age, illness=illness, phone=phone, email=email)
    session.add(patient)
    session.commit()
    
    print(f"\nID: {patient.id} PATIENT: {name} \nAGE: {age} \nILLNESS: {illness} \nTEL-NO: {phone} \nEMAIL ADDRESS: {email}")
    print(f"\nPatient added successfully!")

def update_patient():
    patients = session.query(Patient).all()
    print("\nRegistered patients:")
    for patient in patients:
        print(f"{patient.id}. {patient.name}")

    patient_id = int(input("\nEnter the patient's ID: "))
    patient = session.get(Patient, patient_id)

    if patient:
        patient.name = input(f"Enter new name (current name: {patient.name}): ") or patient.name
        patient.age = int(input(f"Enter new age (current age: {patient.age}): ") or patient.age)
        patient.illess = input(f"Enter new illess (current illness: {patient.illness}): ") or patient.illness
        patient.phone = input(f"Enter new telephone number (current Tel: {patient.phone}): ") or patient.phone
        patient.email = input(f"Enter new email address (current email: {patient.email}): ") or patient.email
        confirm = input("Confirm changes? (yes/no): ").lower()
        if confirm == "yes":
            session.commit()
            print("Patient's information updated successfully!")
        else:
            print("Update canceled.")
    else:
        print("Patient not found.")

def delete_patient():
    patient_id = int(input("\nEnter patient's ID to delete: "))
    patient = session.get(Patient, patient_id)
    if patient:
        confirm = input("Are you sure you want to delete the patient? (yes/no): ")
        if confirm == "yes":
            session.delete(patient)
            session.commit()
            print("Patient deleted successfully!")
        else:
            print("Patient not deleted")
    else:
        print("Patient not found")

def view_patient_info():
    patient_id = int(input("\nEnter ID to view: "))
    patient = session.get(Patient, patient_id)
    if patient:
        print(f"NAME: {patient.name}")
        print(f"AGE: {patient.age}")
        print(f"ILLNESS: {patient.illness}")
        print(f"TEL-NO: {patient.phone}")
        print(f"EMAIL ADDRESS: {patient.email}")
    else:
            print("No patient history")

def view_all_patients():
    #Returning lists of all patients
    patients = session.query(Patient).all()
    if patients:
        for patient in patients:
            print(f"\n{patient.id}. {patient.name} ({patient.age} years old, {patient.illness})")
    else:
        print("No patients found")
        
#--------------- DOCTORS DATABASE ------------

def create_doctor():
    name = input("Enter doctor's name: ")
    specialty = input("Enter doctor's specialty: ")

    doctor = Doctor(name=name, specialty=specialty)
    session.add(doctor)
    session.commit()
    print(f"\nID: {doctor.id} \nNAME: Dr.{doctor.name} \nSPECIALTY: {doctor.specialty}")
    print("\nDoctor added successfully!")

def update_doctor():
    doctor_id = int(input("Enter doctor's ID: "))
    doctor = session.get(Doctor, doctor_id)

    if doctor:
        doctor.name = input(f"Enter new name(current name: {doctor.name}): ") or doctor.name
        doctor.specialty = input(f"Enter new specialty: (current: {doctor.specialty}): ") or doctor.specialty
        session.commit()
        print("Doctor updated successfully!")
    else:
        print("Doctor not found")

def delete_doctor():
    doctor_id = int(input("Enter doctor's ID to delete: "))
    doctor = session.get(Doctor, doctor_id)
    if doctor:
        session.delete(doctor)
        session.commit()
        print("Doctor deleted successfully!")
    else:
        print("Doctor not found")
    
def view_doctor_info():
    doctor_id = int(input("Enter ID to view: "))
    doctor = session.get(Doctor, doctor_id)
    if doctor:
        print(f"\nNAME: Dr. {doctor.name}")
        print(f"SPECIALTY: {doctor.specialty}")
    else:
        print("No doctor history, Doctor not found")

def view_all_doctors():
    #Returning lists of all doctors
    doctors = session.query(Doctor).all()
    if doctors:
        for doctor in doctors:
            print(f"\n{doctor.id}. Dr.{doctor.name} ({doctor.specialty})")
    else:
        print("No doctors found")
        

# ---------------SCHEDULING APPOINTMENTS DATABASE-----------
def schedule_appointment():
    patients = session.query(Patient).all()
    doctors = session.query(Doctor).all()

    # if not patients or doctors:
    #     print("Make sure you have both patients and doctors are registered")
    #     return
    print("\nAvailable Patients:")
    for patient in patients:
        print(f"{patient.id}. {patient.name} ({patient.age})Y/O, {patient.illness}")

    print("\nAvailable Doctors:")
    for doctor in doctors:
        print(f"{doctor.id}. Dr.{doctor.name} ({doctor.specialty})")

    patient_id = int(input("\nSelect patient ID: "))
    doctor_id = int(input("Select doctor ID: "))
    date = input("Enter appointment date (DD-MM-YYYY): ")

# Confirmation  

    patient = session.get(Patient, patient_id)
    doctor = session.get(Doctor, doctor_id)

    if not patient:
        print("Invalid patient ID")
    if not doctor:
        print("Invalid doctor ID")

    print(f"\nScheduling Appointment:")
    print(f"    Patient: {patient.name} ({patient.illness})")
    print(f"    Doctor: Dr.{doctor.name} ({doctor.specialty})")
    print(f"    Date: {date}")

    #Confirming appointment scheduled
    confirm = input("Confirm appointment? (yes/no): ").lower()
    if confirm == "yes":
        appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id, date=date)
        session.add(appointment)
        session.commit()
        print("Appointment scheduled successfully!")
    else:
        print("Appointment cancelled")

def update_appointment():
    appointment_id = int(input("Enter appointment ID to edit: "))
    appointment = session.get(Appointment, appointment_id)
    if appointment:
        patient = session.get(Patient, appointment.patient_id)
        doctor = session.get(Doctor, appointment.doctor_id)

        print(f"\nCurrent details:")
        print(f"  Patient: {patient.name} ({patient.illness})")
        print(f"  Doctor: Dr.{doctor.name} ({doctor.specialty})")
        print(f"  Date: {appointment.date}")

        print("\nAvailable Patients:")
        patients = session.query(Patient).all()
        for patient in patients:
            print(f"{patient.id}. {patient.name} ({patient.illness})")

        print("\nAvailable Doctor:")
        doctors = session.query(Doctor).all()
        for doctor in doctors:
            print(f"{doctor.id}. Dr.{doctor.name} ({doctor.specialty})")

        new_patient_id = input(f"\nEnter new patient ID: (current ID: {appointment.patient_id}): ") or appointment.patient_id
        new_doctor_id = input(f"Enter new doctor ID: (current ID: {appointment.doctor_id}): ") or appointment.doctor_id
        new_date = input(f"Enter new date (current date: {appointment.date}): ") or appointment.date

        # confirming the updated details
        update_patient = session.get(Patient, new_patient_id)
        update_doctor = session.get(Doctor, new_doctor_id)
        print(f"\nUpdated Appointment Details:")
        print(f"  Patient: {update_patient.name} ({update_patient.illness})")
        print(f"  Doctor: Dr.{update_doctor.name} ({update_doctor.specialty})")
        print(f"  Date: {new_date}")
        
        confirm = input("Confirm changes? (yes/no): ").lower()
        if confirm == "yes":
            appointment.patient_id = int(new_patient_id)
            appointment.doctor_id = int(new_doctor_id)
            appointment.date = new_date
            session.commit()
            print("Appointment updated successfully!")
        else:
            print("No updates")
    else:
        print("Appointment not found.")

def delete_appointment():
    appointment_id = int(input("Enter appointment ID to delete: "))
    appointment = session.get(Appointment, appointment_id)
    if appointment:
        confirm = input("Delete appointment? (yes/no): ").lower()
        if confirm == "yes":
            session.delete(appointment)
            session.commit()
            print("Appointment deleted successfully!")
        else:
            print("Deletation canceled")
    else:
        print("Appointment not found.")

def view_all_appointments():
    #Returnig list of all appointments
    appointments = session.query(Appointment).all()
    if not appointments:
        print("No appointments scheduled.")
        return
    
    for appointment in appointments:
        patient = session.get(Patient, appointment.patient_id)
        doctor = session.get(Doctor, appointment.doctor_id)
        print(f"\nAppointments ID: {appointment.id} | Date: {appointment.date}")
        print(f"  Patient: {patient.name} ({patient.illness})")
        print(f"  Doctor: Dr.{doctor.name} ({doctor.specialty})")



def main_menu():
    while True:
        print("\nWelcome to Schedualy, making your work easier is our top priority!")
        print("What would you like to do today?")
        print("\n    PATIENTS ")
        print("1. Add a patient")
        print("2. Update patient information")
        print("3. Delete a patient")
        print("4. View patient's information")
        print("5. All patients")
        print("\n    DOCTORS ")
        print("6. Add a doctor")
        print("7. Update doctor's information")
        print("8. Delete a doctor")
        print("9. View doctor's information")
        print("10. All doctors")
        print("\n    APPOINTMENTS ")
        print("12. Schedule an appointment")
        print("13. Update an appointment")
        print("14. Delete an appointment")
        print("15. View all appointments")
        print("\n00. Exit") 

        choice = input("Select a choice: ")
        if choice == "1":
            create_patient()
        elif choice == "2":
            update_patient()
        elif choice == "3":
            delete_patient()
        elif choice == "4":
            view_patient_info()
        elif choice== "5":
            view_all_patients()
        elif choice == "6":
            create_doctor()
        elif choice == "7":
            update_doctor()
        elif choice == "8":
            delete_doctor()
        elif choice == "9":
            view_doctor_info()
        elif choice == "10":
            view_all_doctors()
        elif choice == "12":
            schedule_appointment()
        elif choice == "13":
            update_appointment()
        elif choice == "14":
            delete_appointment()
        elif choice == "15":
            view_all_appointments()
        elif choice == "00":
            print("Thank you for choosing Schedualy ;)")
            print("Exiting ......")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    init_db()
    main_menu()