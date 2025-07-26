import datetime


from Contact_details import ContactDetails


class Doctor_profile:
    def __init__(self, doctor_id, specialization:str, contact_details:ContactDetails):
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.contact_details = contact_details

        def get_info(self):
            return ({self.doctor_id}), ({self.specialization}), ({self.contact_details})


