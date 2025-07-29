import datetime
import unittest

from patient.contact_details import ContactDetails
from patient.patient import Patient

class TestPatient(unittest.TestCase):
    def test_date_of_birth_must_be_valid(self):
        self.patient = Patient(1,ContactDetails("rasaq","ajape","rasaq@gmail.com","1234567891"),datetime.date(2001,1,23))
        self.assertEqual(self.patient.dob,datetime.date(2001,1,23))

    def test_age_must_be_valid(self):
        self.patient = Patient(1,ContactDetails("rasaq","ajape","rasaq@gmil.com","1234567891"),datetime.date(2001,1,23))
        self.assertEqual(self.patient.age,24)



