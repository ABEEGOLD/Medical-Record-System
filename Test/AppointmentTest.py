import unittest

from Appointment import appointment
from Appointment.appointment import Appointment


class TestAppointment(unittest.TestCase):
    def test_appointment_list_is_empty(self):
        # Appointment.get_appointment_list(self)
        appointments = Appointment.book_appointment(self, "kim", "Dr", "feeling sick", 12)
        self.assertTrue(self, appointments.get_appointment_list(self))
