import unittest

from patient.contact_details import ContactDetails

class TestContactDetails(unittest.TestCase):
    def test_if_first_name_can_be_created(self):
        self.contact_details = ContactDetails("rasaq","ajape","rasaq@email.com","08092397408")
        self.assertEqual(self.contact_details.first_name,"rasaq")

    def test_if_last_name_can_be_created(self):
        self.contact_details = ContactDetails("rasaq","ajape","rasaq@gmail.com","08092397408")
        self.assertEqual(self.contact_details.last_name,"ajape")

    def test_if_email_can_be_created(self):
        self.contact_details = ContactDetails("rasaq","ajape","rasaq@gmail.com","090234455678")
        self.assertEqual(self.contact_details.email,"rasaq@gmail.com")

    def test_if_phone_number_can_be_created(self):
        self.contact_details = ContactDetails("rasaq","ajape","rasaq@gmail.com","08092397408")

    def test_that_name_must_have_atleast_two_character(self):
        self.contact_details = ContactDetails("oka","john","rasaq@gmail.com","08092397408")
        self.assertEqual(self.contact_details.first_name,"oka")
