import unittest
from Doctor.DoctorGo import DoctorRep
from patient.contact_details import ContactDetails

class TestDoctor(unittest.TestCase):
    def test_doctor_contacts_exist(self):
        contact = ContactDetails("firstname", "lastname", "abee23@gmail.com", "09187612343","36")

        doctor = DoctorRep.Doctor_profile(1, "general practitioner", contact)

        self.assertEqual(doctor.contact_details.email, "abee23@gmail.com")
        self.assertEqual(doctor.specialization, "general practitioner")

