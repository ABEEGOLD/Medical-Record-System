import patient.contact_details as ContactDetails

class Doctor:
    def __init__(self, doctor_id: int, contact: ContactDetails, specialty: str):
        if not self._is_valid_specialty(specialty):
            raise ValueError("Invalid specialty - must be 3+ characters")
        if doctor_id <= 0:
            raise ValueError("Doctor ID must be positive")

        self.id = doctor_id
        self.contact = contact
        self.specialty = specialty
        self.appointments = []

    def _is_valid_specialty(self, specialty: str) -> bool:
        return len(specialty.strip()) >= 3

    def __str__(self):
        return f"Dr. {self.contact.last_name} ({self.specialty})"

