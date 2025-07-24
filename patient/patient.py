import datetime

from contact_details import ContactDetails

class Patient:
    def __init__(self, patient_id:int):
        self.id = patient_id
        self.date_of_birth = datetime.date.today()
        self.contact_details = None
        self.medical_history = []
        self.medical_note = []
        self.appointments = []

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

    def book_appointments(self, appointment_date, reason):
        if isinstance(appointment_date, datetime.date) and isinstance(reason, str):
            self.appointments.append({'date': appointment_date, 'reason': reason})
        else:
            raise TypeError('Invalid appointment details')

    def get_summary(self):
        summary = f"""        
        Patient ID: {self.id}
        Contact: {self.contact_details}
        Date of Birth: {self.date_of_birth}
        Medical History: {self.medical_history}
        Medical Notes: {self.medical_note}
        Appointments: {self.appointments}
        """
        return summary.strip()


