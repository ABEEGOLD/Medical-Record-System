import datetime

import tkinter as tk
from patient.clinic_admin import ClinicAdmin,get_validated_choice,get_validated_name,get_validated_date,get_validated_phone,get_validated_email,get_validated_specialty,get_validated_non_empty_string
root = tk.Tk()

def display_menu():
    # label1 = tk.Label(root, text="MERCY CLINIC MANAGEMENT SYSTEM", padx=10, pady=10)
    # label2 = tk.Label(root, text="1. Add Patient", padx=10, pady=10)
    # label3 = tk.Label(root, text="2. Add Doctor", padx=10, pady=10)
    # label4 = tk.Label(root, text="3. View All Patients (with Medical History)", padx=10, pady=10)
    # label5 = tk.Label(root, text="4. view Appointment", padx=10, pady=10)
    # label6 = tk.Label(root, text="5. book Appointment", padx=10, pady=10)
    # label7 = tk.Label(root, text="6. cancel appointment", padx=10, pady=10)
    # label8 = tk.Label(root, text="7. Add Medical Record", padx=10, pady=10)
    # label9 = tk.Label(root, text="8. View Patient Medical Records", padx=10, pady=10)
    # label10= tk.Label(root, text="9. Search Patient/Doctor ", padx=10, pady=10)
    # label11 = tk.Label(root, text="10. Generate Report", padx=10, pady=10)
    # label12= tk.Label(root, text="11. Exit", padx=10, pady=10)

    print("===WELCOME TO MERCY CLINIC MANAGEMENT SYSTEM ===")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. View Appointments")
    print("4. Book Appointment")
    print("5. Cancel Appointment")
    print("6. Add Medical Record")
    print("7. View Patient Medical Records")
    print("8. Search Patient/Doctor")
    print("9. Search Medical Records")
    print("10. Generate Report")
    print("11. Exit")

    # label1.pack()
    # label2.pack()
    # label3.pack()
    # label4.pack()
    # label5.pack()
    # label6.pack()
    # label7.pack()
    # label8.pack()
    # label9.pack()
    # label10.pack()
    # label11.pack()
    # label12.pack()
    # root.mainloop()


def main():

    clinic = ClinicAdmin()

    while True:
        display_menu()
        choice = get_validated_choice("Enter choice (1-11): ", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"])

        if choice == "1":
            print("-- Add Patient --")
            try:
                first_name = get_validated_name("First Name: ")
                last_name = get_validated_name("Last Name: ")
                email = get_validated_email("Email: ", clinic)
                phone = get_validated_phone("Phone: ")
                dob = get_validated_date("Date of Birth (YYYY-MM-DD): ")

                patient = clinic.add_patient(first_name, last_name, email, phone, dob)
                print(f" Patient added successfully: {patient}")
            except ValueError as e:
                print(f" Error: {e}")

        elif choice == "2":
            print("-- Add Doctor --")
            try:
                first_name = get_validated_name("First Name: ")
                last_name = get_validated_name("Last Name: ")
                email = get_validated_email("Email: ", clinic)
                phone = get_validated_phone("Phone: ")
                specialty = get_validated_specialty("Specialty: ")

                doctor = clinic.add_doctor(first_name, last_name, email, phone, specialty)
                print(f"Doctor added successfully: {doctor}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            print("-- All Appointments --")
            appointments = clinic.view_appointments()
            if appointments:
                sorted_appointments = appointments.copy()
                n = len(sorted_appointments)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if sorted_appointments[j].date > sorted_appointments[j + 1].date:
                            temp = sorted_appointments[j]
                            sorted_appointments[j] = sorted_appointments[j + 1]
                            sorted_appointments[j + 1] = temp

                for appt in sorted_appointments:
                    print(appt)
            else:
                print("No appointments found.")

        elif choice == "4":
            print("-- Book Appointment --")
            try:
                if not clinic.patients:
                    print("No patients available. Please add patients first.")
                    continue
                if not clinic.doctors:
                    print("No doctors available. Please add doctors first.")
                    continue

                print("Available Patients:")
                for patient in clinic.patients:
                    print(f"  ID {patient.id}: {patient.contact.first_name} {patient.contact.last_name}")

                print("Available Doctors:")
                for doctor in clinic.doctors:
                    print(f"  ID {doctor.id}: {doctor}")

                patient_ids = []
                for p in clinic.patients:
                    patient_ids.append(str(p.id))

                doctor_ids = []
                for d in clinic.doctors:
                    doctor_ids.append(str(d.id))

                patient_id = int(get_validated_choice("Patient ID: ", patient_ids))
                doctor_id = int(get_validated_choice("Doctor ID: ", doctor_ids))
                date = get_validated_date("Appointment Date (YYYY-MM-DD): ")
                reason = get_validated_non_empty_string("Reason for visit: ")

                appointment = clinic.book_appointment(patient_id, doctor_id, date, reason)
                print(f"Appointment booked successfully: {appointment}")
            except ValueError as e:
                print(f" Error: {e}")

        elif choice == "5":
            print("\n-- Cancel Appointment --")
            appointments = clinic.view_appointments()
            scheduled = []
            for appt in appointments:
                if appt.status == "Scheduled":
                    scheduled.append(appt)

            if scheduled:
                print("Scheduled Appointments:")
                for appt in scheduled:
                    print(appt)

                valid_ids = []
                for appt in scheduled:
                    valid_ids.append(str(appt.id))
                appt_id = int(get_validated_choice("Enter Appointment ID to cancel: ", valid_ids))

                if clinic.cancel_appointment(appt_id):
                    print("Appointment cancelled successfully")
                else:
                    print("Appointment not found or already cancelled")
            else:
                print("No scheduled appointments to cancel.")

        elif choice == "6":
            print("-- Add Medical Record --")
            try:
                if not clinic.patients:
                    print("No patients available. Please add patients first.")
                    continue

                print("Available Patients:")
                for patient in clinic.patients:
                    print(f"  ID {patient.id}: {patient.contact.first_name} {patient.contact.last_name}")

                patient_ids = []
                for p in clinic.patients:
                    patient_ids.append(str(p.id))
                    patient_id = int(get_validated_choice("Patient ID: ", patient_ids))
                    date = get_validated_date("Record Date (YYYY-MM-DD): ")
                    diagnosis = get_validated_non_empty_string("Diagnosis: ")
                    treatment = get_validated_non_empty_string("Treatment: ")
                    doctor_notes = input("Doctor Notes (optional): ").strip()
                    prescribed_medications = input("Prescribed Medications (optional): ").strip()

                record = clinic.add_medical_record(patient_id, date, diagnosis, treatment,
                                               doctor_notes, prescribed_medications)
                print(f"Medical record added successfully: {record}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "7":
            print("\n-- Patient Medical Records --")
            try:
                if not clinic.patients:
                    print("No patients available. Please add patients first.")
                    continue

                print("Available Patients:")
                for patient in clinic.patients:
                    print(f"  ID {patient.id}: {patient.contact.first_name} {patient.contact.last_name}")

                patient_ids = []
                for p in clinic.patients:
                    patient_ids.append(str(p.id))
                    patient_id = int(get_validated_choice("Patient ID: ", patient_ids))
                    records = clinic.get_patient_medical_records(patient_id)

                if records:
                    patient = clinic._find_patient(patient_id)
                    print(f" Medical Records for {patient.contact.first_name} {patient.contact.last_name}:")
                    for record in records:
                        print(f"{record}")
                        print(f"  Treatment: {record.treatment}")
                        if record.doctor_notes:
                            print(f"  Doctor Notes: {record.doctor_notes}")
                        if record.prescribed_medications:
                            print(f"  Medications: {record.prescribed_medications}")
                        print(f"  Created: {record.created_at.strftime('%Y-%m-%d %H:%M')}")
                else:
                    print("No medical records found for this patient.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "8":
            print("-- Search --")
            search_choice = get_validated_choice("1. Search Patients\n2. Search Doctors\nChoose (1-2): ", ["1", "2"])

            if search_choice == "1":
                term = get_validated_non_empty_string("Enter patient name, ID, or email: ")
                results = clinic.search_patients(term)
                print("Patient Search Results:")
            for patient in results:
                print(f"  {patient}")
            if not results:
                print("  No patients found")

            elif search_choice == "2":
                term = get_validated_non_empty_string("Enter doctor name, ID, or specialty: ")
                results = clinic.search_doctors(term)
                print("Doctor Search Results:")
                for doctor in results:
                    print(f"  {doctor}")
                if not results:
                    print("  No doctors found")

        elif choice == "9":
            print("-- Search Medical Records --")
            term = get_validated_non_empty_string("Enter diagnosis, treatment, or medication: ")
            results = clinic.search_medical_records(term)
            print("Medical Records Search Results:")
            for record in results:
                patient = clinic._find_patient(record.patient_id)
                patient_name = f"{patient.contact.first_name} {patient.contact.last_name}" if patient else "Unknown"
                print(f"  {record} - Patient: {patient_name}")
            if not results:
                print("  No medical records found")

        elif choice == "10":
            print(clinic.generate_report())

        elif choice == "11":
            print("Thank you for using Mercy Clinic Management System!")
            break

if __name__ == "__main__":
    main()

