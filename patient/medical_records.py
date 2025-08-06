import datetime

class MedicalRecord:
    def __init__(self, record_id: int, patient_id: int, date: datetime.date,
                 diagnosis: str, treatment: str, doctor_notes: str = "",
                 prescribed_medications: str = ""):
        if not diagnosis.strip():
            raise ValueError("Diagnosis cannot be empty")
        if not treatment.strip():
            raise ValueError("Treatment cannot be empty")

        self.id = record_id
        self.patient_id = patient_id
        self.date = date
        self.diagnosis = diagnosis.strip()
        self.treatment = treatment.strip()
        self.doctor_notes = doctor_notes.strip()
        self.prescribed_medications = prescribed_medications.strip()
        self.created_at = datetime.datetime.now()

    def __str__(self):
        return f"Record {self.id} ({self.date}): {self.diagnosis} - {self.treatment}"
