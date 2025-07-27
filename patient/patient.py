import datetime

class Patient:
    def __init__(self, patient_id:int,contact_details,date_of_birth=datetime.date.today()):
        self.id = patient_id
        self.date_of_birth = datetime.date.today()
        self.contact_details = contact_details
        self.medical_history = []
        self.medical_note = []
        self.appointments = []

    def __str__(self):
        return (
            f"Patient ID: {self.id}, Contact: {self.contact_details}, "
            f"Date of Birth: {self.date_of_birth}, Medical History: {self.medical_history}, "
            f"Medical Notes: {self.medical_note}, Appointments: {len(self.appointments)}"
        )
    @property
    def get_id(self):
        return self.id

    @get_id.setter
    def get_id(self, value):
        if isinstance(value, int):
            self.id = value
        else:
            raise TypeError('ID must be a number')

    @property
    def get_date_of_birth(self):
        return self.date_of_birth

    @get_date_of_birth.setter
    def get_date_of_birth(self, value):
        if isinstance(value, datetime.date):
            self.date_of_birth = value
        else:
            raise TypeError('Date of birth must be a datetime.date')

    @property
    def get_medical_history(self):
        return self.medical_history

    @get_medical_history.setter
    def get_medical_history(self, value):
        if isinstance(value, list):
            self.medical_history = value
        else:
            raise TypeError('Medical history must be a list')

    @property
    def get_medical_note(self):
        return self.medical_note

    @get_medical_note.setter
    def get_medical_note(self, value):
        if isinstance(value, list):
            self.medical_note = value
        else:
            raise TypeError('Medical note must be a list')

    @property
    def get_appointments(self):
        return self.appointments





