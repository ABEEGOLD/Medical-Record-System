import datetime

from patient.contact_details import ContactDetails

from patient.appointment import Appointment

from patient.patient import Patient

from patient.doctor import Doctor

import unittest
class TestAppointment(unittest.TestCase):
    def test_if_appointment_can_be_created(self):
        p1 = Patient(1,ContactDetails("rasaq","ajape","rasaq@mail.com","12345678909"),datetime.date(1994,11,1))
        d1 = Doctor(1,ContactDetails("taye","omolu","omolu@mail.com","1234577654332"),"cardiology")
        appointment = Appointment(1,p1,d1,datetime.date(2025,11,1),"general check up")
        self.assertEqual(appointment.id,1)
        self.assertEqual(appointment.patient,p1)
        self.assertEqual(appointment.doctor,d1)
        self.assertEqual(appointment.date,datetime.date(2025,11,1))
        self.assertEqual(appointment.reason,"general check up")
        self.assertEqual(appointment.status,"Scheduled")