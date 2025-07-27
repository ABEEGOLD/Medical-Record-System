import datetime

class Appointment:
    def __init__(self,appointment_id:int, patient, doctor, reason,date=datetime.date.today()):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = datetime.date.today()
        self.appointment_reason = reason
        self.appointment_is_booked_status = "scheduled"


    def appointments_complete(self):
        return self.appointment_is_booked_status == "completed"
    def appointment_cancelled(self):
        return self.appointment_is_booked_status == "cancelled"

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}, Patient: {self.patient}, Doctor: {self.doctor}, Reason: {self.appointment_reason}, Status: {self.appointment_is_booked_status}"



