import unittest

import datetime

from patient.contact_details import ContactDetails

from patient.patient import Patient

from patient.doctor import Doctor

from patient.appointment import Appointment

from patient.clinic_admin import ClinicAdmin


class TestClinicAdmin(unittest.TestCase):
    def setUp(self):
        self.clinic = ClinicAdmin()

    def test_add_patient(self):
        patient = self.clinic.add_patient("John", "mike", "john@email.com", "1234567890", datetime.date(1990, 1, 1))
        self.assertEqual(patient.contact.first_name, "John")
        self.assertEqual(len(self.clinic.patients), 1)

    def test_add_multiple_patients(self):
        p1 = self.clinic.add_patient("rasaq","ajape","rasaq@mail.com","89786754321985",datetime.date(2012,1,1))
        p2 = self.clinic.add_patient("mufu","ajape","rasaq1@mail.com","89786754321984",datetime.date(2012,2,2))
        p3 = self.clinic.add_patient("okafor","john","rasaq2@mail.com","89786754321983",datetime.date(2012,3,3))
        p4 = self.clinic.add_patient("abigail","orok","rasaq3@mail.com","89786754321982",datetime.date(2012,4,4))
        self.assertEqual(len(self.clinic.patients), 4)
        self.assertEqual(self.clinic.patients[0].contact.first_name,"rasaq")
        self.assertEqual(self.clinic.patients[1].contact.first_name,"mufu")
        self.assertEqual(self.clinic.patients[2].contact.first_name,"okafor")
        self.assertEqual(self.clinic.patients[3].contact.first_name,"abigail")


    def test_add_doctor(self):
        doctor = self.clinic.add_doctor("Jane", "Smith", "jane@email.com", "9876543210", "Cardiology")
        self.assertEqual(doctor.specialty, "Cardiology")
        self.assertEqual(len(self.clinic.doctors), 1)

    def test_add_multiple_doctors(self):
        d1 = self.clinic.add_doctor("rasaq", "Smith", "rasaq@email.com", "9876543211", "Cardiology")
        d2 = self.clinic.add_doctor("john", "Smith", "john@email.com", "9876543212", "Cardiology")
        d3 = self.clinic.add_doctor("okafor", "Smith", "okafor@email.com", "9876543213", "gynecologist")
        d4 = self.clinic.add_doctor("abigail", "Smith", "abagail@email.com", "9876543214", "gynecologist")
        self.assertEqual(len(self.clinic.doctors), 4)
        self.assertEqual(self.clinic.doctors[0].specialty, "Cardiology")
        self.assertEqual(self.clinic.doctors[1].specialty, "Cardiology")
        self.assertEqual(self.clinic.doctors[2].specialty, "gynecologist")
        self.assertEqual(self.clinic.doctors[3].specialty, "gynecologist")
    def test_book_appointment(self):
        p1 = self.clinic.add_patient("John", "mike", "john@email.com", "1234567890", datetime.date(1990, 1, 1))
        d1 = self.clinic.add_doctor("Jane", "Smith", "jane@email.com", "9876543210", "Cardiology")
        appointment = self.clinic.book_appointment(1,1,datetime.date(2025,11,1),"general check up")
        self.assertEqual(appointment.patient.id,1)
        self.assertEqual(appointment.doctor.id,1)
        self.assertEqual(appointment.date,datetime.date(2025,11,1))
        self.assertEqual(appointment.reason,"general check up")
        self.assertEqual(appointment.status,"Scheduled")
        self.assertEqual(len(self.clinic.appointments),1)

    def test_multiple_appointments(self):
        p1 = self.clinic.add_patient("rasaq", "ajape", "rasaq@mail.com", "89786754321985", datetime.date(2012, 1, 1))
        p2 = self.clinic.add_patient("mufu", "ajape", "rasaq1@mail.com", "89786754321984", datetime.date(2012, 2, 2))
        p3 = self.clinic.add_patient("okafor", "john", "rasaq2@mail.com", "89786754321983",datetime.date(2012, 3, 3))
        p4 = self.clinic.add_patient("abigail", "orok", "rasaq3@mail.com", "89786754321982",datetime.date(2012, 4, 4))
        d1 = self.clinic.add_doctor("rasaq", "Smith", "rasaq@email.com", "9876543211", "Cardiology")
        appointment = self.clinic.book_appointment(1, 1, datetime.date(2025, 11, 1), "general check up")
        self.assertEqual(appointment.patient.id, 1)
        self.assertEqual(appointment.doctor.id, 1)
        self.assertEqual(appointment.date, datetime.date(2025, 11, 1))
        self.assertEqual(appointment.reason, "general check up")
        self.assertEqual(appointment.status, "Scheduled")
        self.assertEqual(len(self.clinic.appointments), 1)
        appointment = self.clinic.book_appointment(2, 1, datetime.date(2025, 11, 2), "general check up")
        self.assertEqual(appointment.patient.id, 2)
        self.assertEqual(appointment.doctor.id, 1)
        self.assertEqual(appointment.date, datetime.date(2025, 11, 2))
        self.assertEqual(appointment.reason, "general check up")
        self.assertEqual(appointment.status, "Scheduled")
        self.assertEqual(len(self.clinic.appointments), 2)
        appointment = self.clinic.book_appointment(3, 1, datetime.date(2025, 11, 3), "general check up")
        self.assertEqual(appointment.patient.id, 3)
        self.assertEqual(appointment.doctor.id, 1)
        self.assertEqual(appointment.date, datetime.date(2025, 11, 3))
        self.assertEqual(appointment.reason, "general check up")
        self.assertEqual(appointment.status, "Scheduled")
        self.assertEqual(len(self.clinic.appointments), 3)
        appointment = self.clinic.book_appointment(4, 1, datetime.date(2025, 11, 4), "general check up")
        self.assertEqual(appointment.patient.id, 4)
        self.assertEqual(appointment.doctor.id, 1)
        self.assertEqual(appointment.date, datetime.date(2025, 11, 4))
        self.assertEqual(appointment.reason, "general check up")
        self.assertEqual(appointment.status, "Scheduled")
        self.assertEqual(len(self.clinic.appointments), 4)

    def test_cancel_appointment(self):
        p1 = self.clinic.add_patient("John", "mike", "john@email.com", "1234567890", datetime.date(1990, 1, 1))
        d1 = self.clinic.add_doctor("Jane", "Smith", "jane@email.com", "9876543210", "Cardiology")
        appointment = self.clinic.book_appointment(1, 1, datetime.date(2025, 11, 1), "general check up")
        self.assertEqual(appointment.patient.id, 1)
        self.assertEqual(appointment.doctor.id, 1)
        self.assertEqual(appointment.date, datetime.date(2025, 11, 1))
        self.assertEqual(appointment.reason, "general check up")
        self.assertEqual(appointment.status, "Scheduled")
        self.assertEqual(len(self.clinic.appointments), 1)
        cancelled = self.clinic.cancel_appointment(1)
        self.assertTrue(cancelled)
        self.assertEqual(len(self.clinic.appointments), 1)

    def test_view_appointments(self):
        p1 = self.clinic.add_patient("John", "mike", "john@email.com", "1234567890", datetime.date(1990, 1, 1))
        d1 = self.clinic.add_doctor("Jane", "Smith", "jane@email.com", "9876543210", "Cardiology")
        appt1 = self.clinic.book_appointment(1, 1, datetime.date(2025, 11, 1), "general check up")
        self.assertEqual(len(self.clinic.view_appointments()), 1)

    def test_search_patients(self):
        p1 = self.clinic.add_patient("John", "mike", "mike@email.com", "1234567891", datetime.date(1990, 1, 1))
        p2 = self.clinic.add_patient("John", "sleep", "sleep@email.com", "1234567892", datetime.date(1990, 2, 1))
        p3 = self.clinic.add_patient("John", "okafor", "okafor@email.com", "1234567893", datetime.date(1990, 3, 1))
        p4 = self.clinic.add_patient("John", "abigail", "abigail@email.com", "1234567894", datetime.date(1990, 4, 1))
        self.assertEqual(len(self.clinic.search_patients("mike")), 1)
        self.assertEqual(len(self.clinic.search_patients("sleep")), 1)
        self.assertEqual(len(self.clinic.search_patients("okafor")), 1)
        self.assertEqual(len(self.clinic.search_patients("abigail")), 1)
        self.assertEqual(len(self.clinic.search_patients("john")), 4)

    def test_search_doctors(self):
        d1 = self.clinic.add_doctor("Jane", "abigail", "jane.abigail@email.com", "9876543211", "Cardiology")
        d2 = self.clinic.add_doctor("Jane", "mercy", "jane.mercy@email.com", "9876543212", "orthopedic")
        d3 = self.clinic.add_doctor("Jane", "oliva", "jane.oliva@email.com", "9876543213", "gynecology")
        d4 = self.clinic.add_doctor("Jane", "ola", "jane.ola@email.com", "9876543214", "pediatrician")
        self.assertEqual(len(self.clinic.search_doctors("abigail")), 1)
        self.assertEqual(len(self.clinic.search_doctors("mercy")), 1)
        self.assertEqual(len(self.clinic.search_doctors("oliva")), 1)
        self.assertEqual(len(self.clinic.search_doctors("ola")), 1)
        self.assertEqual(len(self.clinic.search_doctors("jane")), 4)


























if __name__ == '__main__':
    unittest.main()