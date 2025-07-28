import datetime

from patient.contact_details import ContactDetails

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

    def __str__(self):
        return f"Patient {self.id}: {self.contact.first_name} {self.contact.last_name} (Age: {self.age})"

