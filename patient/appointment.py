import datetime

from patient.patient import Patient

from patient.doctor import Doctor

class Appointment:
    def __init__(self, appt_id: int, patient: Patient, doctor: Doctor, date: datetime.date, reason: str):
        self.id = appt_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.reason = reason
        self.status = "Scheduled"

    def cancel(self):
        self.status = "Cancelled"

    def __str__(self):
        return f"Appointment {self.id}: {self.date} | {self.patient.contact.first_name} {self.patient.contact.last_name} with {self.doctor} for {self.reason} [{self.status}]"

