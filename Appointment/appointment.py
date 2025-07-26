class Appointment:
    def __init__(self, appointment_list, appointment_is_booked_status, appointment_id):
        self.appointment_list = []
        self.appointment_is_booked_status = False
        self.appointment_id = 0

    def book_appointment(self, patient, doctor, reason, datetime):
        self.appointment_list.extend([patient, doctor, reason, datetime])
        self.appointment_is_booked_status = True
        self.appointment_id += 1

    def get_appointments(self):
        return {self.appointment_list, self.appointment_is_booked_status}

    def get_appointment_status(self):
        return self.appointment_is_booked_status

    def get_appointment_list(self):
        return self.appointment_list

    def cancel_appointment(self, appointment_id):
        self.appointment_is_booked_status = False
        for patient in self.appointment_list:
            if self.appointment_id == patient:
                self.appointment_list.remove(patient)
        return self.appointment_list

