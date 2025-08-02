import datetime

import tkinter as tk

from typing import List, Dict

from patient.patient import Patient

from patient.contact_details import ContactDetails

from patient.doctor import Doctor

from patient.appointment import Appointment

class ClinicAdmin(tk.Tk):
    def __init__(self):
        self.patients: List[Patient] = []
        self.doctors: List[Doctor] = []
        self.appointments: List[Appointment] = []
        self.next_patient_id = 1
        self.next_doctor_id = 1
        self.next_appointment_id = 1

    def add_patient(self, first_name: str, last_name: str, email: str, phone: str, dob: datetime.date) -> Patient:
        if self._email_exists(email):
            raise ValueError("Email already exists in system")

        contact = ContactDetails(first_name, last_name, email, phone)
        patient = Patient(self.next_patient_id, contact, dob)
        self.patients.append(patient)
        self.next_patient_id += 1
        return patient

    def add_doctor(self, first_name: str, last_name: str, email: str, phone: str, specialty: str) -> Doctor:
        if self._email_exists(email):
            raise ValueError("Email already exists in system")

        contact = ContactDetails(first_name, last_name, email, phone)
        doctor = Doctor(self.next_doctor_id, contact, specialty)
        self.doctors.append(doctor)
        self.next_doctor_id += 1
        return doctor

    def add_medical_record(self, patient_id: int, date: datetime.date, diagnosis: str,
                           treatment: str) -> Dict:
        patient = self._find_patient(patient_id)
        if not patient:
            raise ValueError(f"Patient with ID {patient_id} not found")

        return patient.add_medical_record(date, diagnosis, treatment)

    def get_patient_medical_history(self, patient_id: int) -> List[Dict]:
        patient = self._find_patient(patient_id)
        if not patient:
            raise ValueError(f"Patient with ID {patient_id} not found")
        return patient.get_medical_history()

    def search_medical_records(self, term: str) -> List[Dict]:
        term = term.lower()
        results = []
        for patient in self.patients:
            for record in patient.medical_history:
                if (term in record['diagnosis'].lower() or
                    term in record['treatment'].lower()):
                    record_with_patient = record.copy()
                    record_with_patient['patient_id'] = patient.id
                    record_with_patient['patient_name'] = f"{patient.contact.first_name} {patient.contact.last_name}"
                    results.append(record_with_patient)
        return results

    def display_patient_with_history(self, patient: Patient):
        print(f"\n{patient}")
        print(f"  Email: {patient.contact.email}")
        print(f"  Phone: {patient.contact.phone}")
        print(f"  DOB: {patient.dob}")

        if patient.medical_history:
            print(f"  Medical Records: {len(patient.medical_history)} record(s)")
            print("  Recent Medical History:")
            recent_records = patient.get_medical_history()[:3]  # Get 3 most recent
            for record in recent_records:
                print(f"    • {record['date']}: {record['diagnosis']} - {record['treatment']}")
        else:
            print("  Medical Records: No records found")

    def prompt_medical_history(self, patient_id: int):
        try:
            patient = self._find_patient(patient_id)
            if not patient:
                raise ValueError(f"Patient with ID {patient_id} not found")

            records = patient.get_medical_history()

            if records:
                print(f"=== FULL MEDICAL HISTORY FOR {patient.contact.first_name} {patient.contact.last_name} ===")
                for index, record in enumerate(records, 1):
                    print(f"{index}. {record['date']}: {record['diagnosis']}")
                    print(f"   Treatment: {record['treatment']}")
                    print(f"   Added: {record['created_at'].strftime('%Y-%m-%d %H:%M')}")
            else:
                print(f"No medical history found for {patient.contact.first_name} {patient.contact.last_name}")
        except ValueError as e:
            print(f"✗ Error: {e}")

    def _find_patient(self, patient_id: int):
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    def _find_doctor(self, doctor_id: int):
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        return None


    def book_appointment(self, patient_id: int, doctor_id: int, date: datetime.date, reason: str) -> Appointment:
        if date < datetime.date.today():
            raise ValueError("Cannot book appointment in the past")

        patient = self._find_patient(patient_id)
        doctor = self._find_doctor(doctor_id)

        if not patient:
            raise ValueError(f"Patient with ID {patient_id} not found")
        if not doctor:
            raise ValueError(f"Doctor with ID {doctor_id} not found")

        if self._doctor_busy(doctor_id, date):
            raise ValueError("Doctor already has an appointment at this time")

        appointment = Appointment(self.next_appointment_id, patient, doctor, date, reason)
        self.appointments.append(appointment)
        self.next_appointment_id += 1

        patient.appointments.append(appointment)
        doctor.appointments.append(appointment)
        return appointment

    def cancel_appointment(self, appt_id: int) -> bool:
        for appointment in self.appointments:
            if appointment.id == appt_id and appointment.status == "Scheduled":
                appointment.cancel()
                return True
        return False

    def view_appointments(self) -> List[Appointment]:
        return self.appointments

    def search_patients(self, find: str) -> List[Patient]:
        find = find.lower()
        results = []
        for patient in self.patients:
            if (find in str(patient.id) or
                    find in patient.contact.first_name.lower() or
                    find in patient.contact.last_name.lower() or
                    find in patient.contact.email.lower()):
                results.append(patient)
        return results

    def search_doctors(self, find: str) -> List[Doctor]:
        find = find.lower()
        results = []
        for doctor in self.doctors:
            if (find in str(doctor.id) or
                    find in doctor.contact.first_name.lower() or
                    find in doctor.contact.last_name.lower() or
                    find in doctor.specialty.lower()):
                results.append(doctor)
        return results

    def _sort_appointments_by_date(self, appointments):
        for index in range(len(appointments)):
            for data in range(len(appointments) - 1 - index):
                if appointments[data].date < appointments[data + 1].date:
                    appointments[data], appointments[data + 1] = appointments[data + 1], appointments[data]
        return appointments

    def _sort_records_by_date(self, records):
        for index in range(len(records)):
            for data in range(len(records) - 1 - index):
                if records[data]['date'] < records[data + 1]['date']:
                    records[data], records[data + 1] = records[data + 1], records[data]
        return records


    def generate_report(self) -> str:
        total_patients = len(self.patients)
        total_doctors = len(self.doctors)
        total_appointments = len(self.appointments)

        total_medical_records = 0
        for patient in self.patients:
            total_medical_records += len(patient.medical_history)

            scheduled_appointments = 0
            cancelled_appointments = 0
            for appt in self.appointments:
                if appt.status == "Scheduled":
                    scheduled_appointments += 1
                elif appt.status == "Cancelled":
                    cancelled_appointments += 1

            report = f"""
                === CLINIC REPORT ===
                Total Patients: {total_patients}
                Total Doctors: {total_doctors}
                Total Appointments: {total_appointments}
                Total Medical Records: {total_medical_records}
                Scheduled Appointments: {scheduled_appointments}
                Cancelled Appointments: {cancelled_appointments}

            Recent Appointments:
            """
            sorted_appointments = self._sort_appointments_by_date(self.appointments.copy())
            recent_appointments = sorted_appointments[:5]
            for appt in recent_appointments:
                report += f"  {appt}"

            all_records = []
            for patient in self.patients:
                for record in patient.medical_history:
                    record_with_patient = {
                        'date': record['date'],
                        'diagnosis': record['diagnosis'],
                        'treatment': record['treatment'],
                        'patient_name': f"{patient.contact.first_name} {patient.contact.last_name}"
                    }
                    all_records.append(record_with_patient)

            report += "Recent Medical Records: "
            sorted_records = self._sort_records_by_date(all_records.copy())
            recent_records = sorted_records[:5]
            for record in recent_records:
                report += f"  {record['date']}: {record['diagnosis']} - {record['treatment']} - Patient: {record['patient_name']}\n"

            return report





    def _email_exists(self, email: str) -> bool:
        for patient in self.patients:
            if patient.contact.email == email:
                return True
        for doctor in self.doctors:
            if doctor.contact.email == email:
                return True
        return False

    def _doctor_busy(self, doctor_id: int, date: datetime.date) -> bool:
        for appt in self.appointments:
            if appt.doctor.id == doctor_id and appt.date == date and appt.status == "Scheduled":
                return True
        return False


def get_date_input(collect: str) -> datetime.date:
    while True:
        try:
            date_str = input(collect).strip()
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")

