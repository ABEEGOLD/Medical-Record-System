import datetime

from patient.contact_details import ContactDetails

from typing import List, Dict

class Patient:
    def __init__(self, patient_id: int, contact: ContactDetails, dob: datetime.date):
        if not self._is_valid_age(dob):
            raise ValueError("Invalid date of birth - age must be between 0-150")
        if patient_id <= 0:
            raise ValueError("Patient ID must be positive")

        self.id = patient_id
        self.contact = contact
        self.dob = dob
        self.appointments = []
        self.medical_history = []


    def _is_valid_age(self, dob: datetime.date) -> bool:
        today = datetime.date.today()
        if dob > today:
            return False
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return 0 <= age <= 150

    @property
    def age(self):
        today = datetime.date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def add_medical_record(self, date: datetime.date, diagnosis: str, treatment: str):
        if not diagnosis.strip():
            raise ValueError("Diagnosis cannot be empty")
        if not treatment.strip():
            raise ValueError("Treatment cannot be empty")

        record = {
            'date': date,
            'diagnosis': diagnosis.strip(),
            'treatment': treatment.strip(),
            'created_at': datetime.datetime.now()
        }
        self.medical_history.append(record)
        return record

    def get_medical_history(self) -> List[Dict]:
        history = self.medical_history.copy()
        for index in range(len(history)):
            for data in range(len(history) - 1 - index):
                if history[data]['date'] < history[data + 1]['date']:
                    history[data], history[data + 1] = history[data + 1], history[data]
        return history

    def __str__(self):
        return f"Patient {self.id}: {self.contact.first_name} {self.contact.last_name} (Age: {self.age})"

