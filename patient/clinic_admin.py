import datetime

import re

from typing import List

from patient.patient import Patient

from patient.medical_records import MedicalRecord

from patient.contact_details import ContactDetails

from patient.doctor import Doctor

from patient.appointment import Appointment

class ClinicAdmin:
    def __init__(self):
        self.patients: List[Patient] = []
        self.doctors: List[Doctor] = []
        self.appointments: List[Appointment] = []
        self.medical_records: List[MedicalRecord] = []
        self.next_patient_id = 1
        self.next_doctor_id = 1
        self.next_appointment_id = 1
        self.next_record_id = 1

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
                           treatment: str, doctor_notes: str = "", prescribed_medications: str = "") -> MedicalRecord:
        patient = self._find_patient(patient_id)
        if not patient:
            raise ValueError(f"Patient with ID {patient_id} not found")

        record = MedicalRecord(self.next_record_id, patient_id, date, diagnosis,
                               treatment, doctor_notes, prescribed_medications)
        self.medical_records.append(record)
        patient.add_medical_record(record)
        self.next_record_id += 1
        return record

    def get_patient_medical_records(self, patient_id: int) -> List[MedicalRecord]:
        patient = self._find_patient(patient_id)
        if not patient:
            raise ValueError(f"Patient with ID {patient_id} not found")
        return patient.get_medical_history()

    def search_medical_records(self, term: str) -> List[MedicalRecord]:
        term = term.lower()
        results = []
        for record in self.medical_records:
            if (term in record.diagnosis.lower() or
                    term in record.treatment.lower() or
                    term in record.doctor_notes.lower() or
                    term in record.prescribed_medications.lower()):
                results.append(record)
        return results


    def _find_patient(self, patient_id: int) ->[Patient]:
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    def _find_doctor(self, doctor_id: int) ->[Doctor]:
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

    def search_patients(self, collect: str) -> List[Patient]:
        collect = collect.lower()
        results = []
        for patient in self.patients:
            if (collect in str(patient.id) or
                    collect in patient.contact.first_name.lower() or
                    collect in patient.contact.last_name.lower() or
                    collect in patient.contact.email.lower()):
                results.append(patient)
        return results

    def search_doctors(self, take: str) -> List[Doctor]:
        take = take.lower()
        results = []
        for doctor in self.doctors:
            if (take in str(doctor.id) or
                    take in doctor.contact.first_name.lower() or
                    take in doctor.contact.last_name.lower() or
                    take in doctor.specialty.lower()):
                results.append(doctor)
        return results

    def generate_report(self) -> str:
        total_patients = len(self.patients)
        total_doctors = len(self.doctors)
        total_appointments = len(self.appointments)
        total_medical_records = len(self.medical_records)
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
        sorted_appointments = self.appointments.copy()
        n = len(sorted_appointments)
        for i in range(n):
            for j in range(0, n - i - 1):
                if sorted_appointments[j].date < sorted_appointments[j + 1].date:
                    temp = sorted_appointments[j]
                    sorted_appointments[j] = sorted_appointments[j + 1]
                    sorted_appointments[j + 1] = temp

        recent_appointments = []
        count = 0
        for appt in sorted_appointments:
            if count < 5:
                recent_appointments.append(appt)
                count += 1
            else:
                break

        for appt in recent_appointments:
            report += f" {appt}\n"

        report += "\nRecent Medical Records:\n"

        sorted_records = self.medical_records.copy()
        n = len(sorted_records)
        for i in range(n):
            for j in range(0, n - i - 1):
                if sorted_records[j].date < sorted_records[j + 1].date:
                    # Swap records
                    temp = sorted_records[j]
                    sorted_records[j] = sorted_records[j + 1]
                    sorted_records[j + 1] = temp

        recent_records = []
        count = 0
        for record in sorted_records:
            if count < 5:
                recent_records.append(record)
                count += 1
            else:
                break

        for record in recent_records:
            patient = self._find_patient(record.patient_id)
            patient_name = f"{patient.contact.first_name} {patient.contact.last_name}" if patient else "Unknown"
            report += f"{record} - Patient: {patient_name}\n"

        return report

    def _email_exists(self, email: str) -> bool:
        email = email.lower().strip()
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


def get_validated_name(prompt: str) -> str:
    while True:
        name = input(prompt).strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            continue
        if not name.isalpha():
            print("Name must contain only alphabetic characters. Please try again.")
            continue
        if len(name) < 2:
            print("Name must be at least 2 characters long. Please try again.")
            continue
        return name


def get_validated_email(prompt: str, clinic: ClinicAdmin) -> str:
    while True:
        email = input(prompt).strip()
        if not email:
            print("Email cannot be empty. Please try again.")
            continue

        if clinic._email_exists(email):
            print("This email already exists in the system. Please use a different email.")
            continue

        email_lower = email.lower().strip()

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email_lower):
            print("Invalid email format. Please enter a valid email (e.g., user@example.com).")
            continue

        if email_lower.count('@') != 1:
            print("Email must contain exactly one @ symbol.")
            continue

        local, domain = email_lower.split('@')

        if len(local) < 1 or len(local) > 64:
            print("Email local part must be 1-64 characters long.")
            continue
        if local.startswith('.') or local.endswith('.'):
            print("Email local part cannot start or end with a period.")
            continue
        if '..' in local:
            print("Email local part cannot contain consecutive periods.")
            continue

        if len(domain) < 1 or len(domain) > 255:
            print("Email domain must be 1-255 characters long.")
            continue
        if domain.startswith('-') or domain.endswith('-'):
            print("Email domain cannot start or end with a hyphen.")
            continue
        if '..' in domain:
            print("Email domain cannot contain consecutive periods.")
            continue

        return email


def get_validated_phone(prompt: str) -> str:
    while True:
        phone = input(prompt).strip()
        if not phone:
            print("Phone number cannot be empty. Please try again.")
            continue
        if not phone.isdigit():
            print("Phone number must contain only digits. Please try again.")
            continue
        if len(phone) < 10:
            print("Phone number must be at least 10 digits long. Please try again.")
            continue
        return phone


def get_validated_specialty(prompt: str) -> str:
    while True:
        specialty = input(prompt).strip()
        if not specialty:
            print("Specialty cannot be empty. Please try again.")
            continue
        if len(specialty) < 3:
            print("Specialty must be at least 3 characters long. Please try again.")
            continue
        return specialty


def get_validated_date(prompt: str) -> datetime.date:
    while True:
        try:
            date_str = input(prompt).strip()
            if not date_str:
                print("Date cannot be empty. Please try again.")
                continue
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD (e.g., 2024-01-15).")


def get_validated_integer(prompt: str, min_value: int = None, max_value: int = None) -> int:
    while True:
        try:
            value_str = input(prompt).strip()
            if not value_str:
                print("Value cannot be empty. Please try again.")
                continue
            value = int(value_str)
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}. Please try again.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}. Please try again.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_validated_non_empty_string(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if not value:
            print("This field cannot be empty. Please try again.")
            continue
        return value


def get_validated_choice(prompt: str, valid_choices: List[str]) -> str:
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please select from: {', '.join(valid_choices)}")
