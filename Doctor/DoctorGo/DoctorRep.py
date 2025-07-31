import datetime
from patient.contact_details import ContactDetails  # Assuming this is correct

class Doctor_profile:

    def __init__(self, doctor_id: str, specialization: str, contact_details: ContactDetails, schedule_appointment: int):
        self.doctor_id = f"D{str(doctor_id).zfill(3)}"
        self.specialization = specialization
        self.contact_details = contact_details
        self.schedule_appointment = schedule_appointment
        self.appointments = []

    def get_info(self):
        return ({self.doctor_id}), ({self.specialization}), ({self.contact_details})

    def getDoctorContactDetails(self):
        return self.contact_details

    def getDoctorName(self):
        return self.doctor_id

    def getDoctorSpecialization(self):
        return self.specialization

    def assign_doctor(self):
        return self.doctor_id, self.specialization, self.contact_details

    def isBooked(self, appointment_date: datetime.date):
        for appt in self.appointments:
            if appt.date == appointment_date:
                return True
        return False

    def isNotBooked(self, appointment_date: datetime.date):
        for appt in self.appointments:
            if appt.date == appointment_date:
                return False
        return True

    def get_patient_info(self):
        return self.Patient_id,self.contact_details, self.date_of_birth,self.medical_history,self.medical_note



    def __str__(self):
        return f"Dr. {self.contact_details.first_name} {self.contact_details.last_name} ({self.specialization})"

    def cancel_appointment(self, appointment_id):
        for appt in self.appointments:
            if appt.id == appointment_id:
                self.appointments.remove(appt)
                return True
    def invalidate_appointment(self):
        pass


