import datetime

import tkinter as tk

from patient.clinic_admin import ClinicAdmin, get_date_input

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


    print("=== WELCOME MERCY CLINIC MANAGEMENT SYSTEM ===")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. View All Patients (with Medical History)")
    print("4. View Appointments")
    print("5. Book Appointment")
    print("6. Cancel Appointment")
    print("7. Add Medical Record")
    print("8. View Patient Medical Records")
    print("9. Search Patient/Doctor")
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
        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            print("== Add Patient ==")
            try:
                first_name = input("First Name: ").strip()
                last_name = input("Last Name: ").strip()
                email = input("Email: ").strip()
                phone = input("Phone: ").strip()
                dob = get_date_input("Date of Birth (YYYY-MM-DD): ")

                patient = clinic.add_patient(first_name, last_name, email, phone, dob)
                print(f" Patient added successfully: {patient}")
            except ValueError as e:
                print(f" Error: {e}")

        elif choice == "2":
            print("== Add Doctor ==")
            try:
                first_name = input("First Name: ").strip()
                last_name = input("Last Name: ").strip()
                email = input("Email: ").strip()
                phone = input("Phone: ").strip()
                specialty = input("Specialty: ").strip()

                doctor = clinic.add_doctor(first_name, last_name, email, phone, specialty)
                print(f" Doctor added successfully: {doctor}")
            except ValueError as e:
                print(f" Error: {e}")

        elif choice == "3":
            print("\n-- All Patients with Medical History --")
            if clinic.patients:
                for patient in clinic.patients:
                    clinic.display_patient_with_history(patient)

                while True:
                    prompt = input("Enter Patient ID for full medical history (or 'back' to return): ").strip()
                    if prompt.lower() == 'back':
                        break
                    try:
                        patient_id = int(prompt)
                        clinic.prompt_medical_history(patient_id)
                    except ValueError:
                        print("Please enter a valid Patient ID or 'back'")
            else:
                print("No patients found.")


        elif choice == "4":
            print("== All Appointments ==")
            appointments = clinic.view_appointments()
            if appointments:
                for index in range(len(appointments)):
                    for data in range(len(appointments) - 1):
                        if appointments[data].date > appointments[data + 1].date:
                            appointments[data], appointments[data + 1] = appointments[data + 1], appointments[data]

                for appt in appointments:
                    print(appt)
            else:
                print("No appointments found.")

        elif choice == "5":
            print("== Book Appointment ==")
            try:
                print("Available Patients:")
                for patient in clinic.patients:
                    print(f"  ID {patient.id}: {patient.contact.first_name} {patient.contact.last_name}")

                print("Available Doctors:")
                for doctor in clinic.doctors:
                    print(f"  ID {doctor.id}: {doctor}")

                patient_id = int(input("Patient ID: "))
                doctor_id = int(input("Doctor ID: "))
                date = get_date_input("Appointment Date (YYYY-MM-DD): ")
                reason = input("Reason for visit: ").strip()

                appointment = clinic.book_appointment(patient_id, doctor_id, date, reason)
                print(f" Appointment booked successfully: {appointment}")
            except (ValueError, KeyError) as e:
                print(f" Error: {e}")

        elif choice == "6":
            print("== Cancel Appointment ==")
            appointments = clinic.view_appointments()
            scheduled = [appt for appt in appointments if appt.status == "Scheduled"]

            if scheduled:
                print("Scheduled Appointments:")
                for appt in scheduled:
                    print(appt)

                try:
                    appt_id = int(input("Enter Appointment ID to cancel: "))
                    if clinic.cancel_appointment(appt_id):
                        print(" Appointment cancelled successfully")
                    else:
                        print(" Appointment not found or already cancelled")
                except ValueError:
                    print(" Invalid appointment ID")
            else:
                print("No scheduled appointments to cancel.")

        elif choice == "7":
            print("==Add Medical Record==")
            try:
                print("Available Patients:")
                for patient in clinic.patients:
                    clinic.display_patient_with_history(patient)

                patient_id = int(input("Patient ID: "))
                date = get_date_input("Record Date (YYYY-MM-DD): ")
                diagnosis = input("Diagnosis: ").strip()
                treatment = input("Treatment: ").strip()
                record = clinic.add_medical_record(patient_id, date, diagnosis, treatment)
                print(f"Medical record added successfully: {record['date']} - {record['diagnosis']}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "8":
            print("==Patient Medical Records==")
            try:
                print("Available Patients:")
                for patient in clinic.patients:
                    clinic.display_patient_with_history(patient)

                patient_id = int(input("\nPatient ID: "))
                clinic.prompt_medical_history(patient_id)
            except ValueError as e:
                print(f"Error: {e}")



        elif choice == "9":
            print("== Search ==")
            print("1. Search Patients")
            print("2. Search Doctors")
            search_choice = input("Choose (1-2): ").strip()

            if search_choice == "1":
                find = input("Enter patient name, ID, or email: ").strip()
                results = clinic.search_patients(find)
                print("Patient Search Results:")
                for patient in results:
                    print(f"  {patient}")
                if not results:
                    print("  No patients found")

            elif search_choice == "2":
                find = input("Enter doctor name, ID, or specialty: ").strip()
                results = clinic.search_doctors(find)
                print("Doctor Search Results:")
                for doctor in results:
                    print(f"  {doctor}")
                if not results:
                    print("  No doctors found")

        elif choice == "10":
            print(clinic.generate_report())

        elif choice == "11":
            print("Thank you for using Mercy Clinic Management System!")
            break

        else:
            print("Invalid choice. Please select 1-8.")

if __name__ == "__main__":
    main()

