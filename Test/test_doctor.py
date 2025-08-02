import unittest

from patient.doctor import Doctor

from patient.contact_details import ContactDetails

class TestDoctor(unittest.TestCase):
    def test_doctor_specialty(self):
        doc = Doctor(1, ContactDetails("john","okafor","john@mail.com","908765432123"),"cardiologist")
        self.assertEqual(doc.specialty, "cardiologist")

    def test_for_multiple_specialty(self):
        doc = Doctor(1, ContactDetails("john","okafor","john1@mail.com","908765432123"),"cardiologist")
        doc1 = Doctor(1, ContactDetails("john","noble","john2@mail.com","908765432124"),"gynecologist")
        doc2 = Doctor(1, ContactDetails("john","wicked","john3@mail.com","908765432125"),"orthopedic")
        doc3 = Doctor(1, ContactDetails("john","sleep","john4@mail.com","908765432126"),"pediatrician")
        self.assertEqual(doc.specialty,"cardiologist")
        self.assertEqual(doc1.specialty,"gynecologist")
        self.assertEqual(doc2.specialty,"orthopedic")
        self.assertEqual(doc3.specialty,"pediatrician")



    def test_if_specialty_length_is_valid(self):
        doc = Doctor(1, ContactDetails("john","okafor","john@mail.com","908765432123"),"car")
        self.assertEqual(doc.specialty,"car")

