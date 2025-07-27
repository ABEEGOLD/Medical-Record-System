from patient.contact_details import ContactDetails

class DoctorProfile:
    def __init__(self, doctor_id, specialization:str, contact_details:ContactDetails):
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.contact_details = contact_details

    def __str__(self):
        return f"Doctor ID: {self.doctor_id}, Specialization: {self.specialization}, Contact: {self.contact_details}"



