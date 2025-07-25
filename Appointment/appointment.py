import Appointment


class appointment(object):
    def __init__(self, appointment):
        self.appointment_list = []
        self.appointment_is_booked_status = False
        self.appointment_ID = 0


    def book_appointment(self, Patient, Doctor, Reason, datetime):
        self.appointment_list.extend([Patient, Doctor, Reason, datetime])
        self.appointment_is_booked_status = True
        self.appointment_ID += 1

    def get_appointments(self):
        return {self.appointment_list, self.appointment_is_booked_status}

    def get_appointment_status(self):
        return self.appointment_is_booked_status

    def get_appointment_list(self):
        return self.appointment_list

    def cancel_appointment(self, appointment_ID):
        self.appointment_is_booked_status = False
        for patient in self.appointment_list:
            if self.appointment_ID == patient:
                self.appointment_list.remove(patient)

