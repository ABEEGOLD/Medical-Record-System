import unittest


from Doctor.DoctorGo import DoctorRep

from patient.contact_details import ContactDetails


class TestDoctor(unittest.TestCase):
    def SetUp(self):
        contact = ContactDetails("dr smith", "joe", "abee23@gmail.com", 9187612343)
        self.doctor = DoctorRep.Doctor_profile("001","general doctor",contact,1)

    def test_doctor_contacts_exist(self):
        contact = ContactDetails("dr smith", "joe", "abee23@gmail.com", 9187612343)
        doctor = DoctorRep.Doctor_profile("001", "general practitioner", contact,1)

        self.assertEqual(doctor.contact_details.email, "abee23@gmail.com")
        self.assertEqual(doctor.specialization, "general practitioner")

    def test_doctor_id_format(self):
        contact = ContactDetails("firstname", "lastname", "abee23@gmail.com", 34567890223)
        doctor = DoctorRep.Doctor_profile("001", "general practitioner", contact,1)
        self.assertRegex(doctor.doctor_id, r'^D\d{3}$')

    def test_doctor_specialization(self):
        contact = ContactDetails("Dr grey", "lance", "lance2@gmail.com", 93456712343)
        doctor = DoctorRep.Doctor_profile("001", "Dentistry", contact,1)
        self.assertEqual(doctor.specialization,"Dentistry")

    def test_doctor_schedule_appointment(self):
        contact = ContactDetails("Dr grey", "lance", "lance2@gmail.com", 93456712343)
        doctor = DoctorRep.Doctor_profile("001", "Dentistry", contact,1)
        self.assertEqual(doctor.schedule_appointment, 1, "doctor schedules appointment")

    def test_doctor_appointment_is_booked(self):
        contact = ContactDetails("Dr grey", "lance", "lance2@gmail.com", 93456712343)
        doctor = DoctorRep.Doctor_profile("001", "Dentistry", contact,1)
        self.assertEqual(doctor.isBooked(11 - 0o5 - 99), False, "doctor is booked")


    def test_doctor_appointment_is_not_booked(self):
        contact = ContactDetails("Dr grey", "lance", "lance2@gmail.com", 93456712343)
        doctor = DoctorRep.Doctor_profile("001", "Dentistry", contact, 1)
        self.assertEqual(doctor.isNotBooked(11 - 0o5 - 99), True, "doctor is not booked")

    def test_cancel_appointment(self):
        contact = ContactDetails("Dr grey", "lance", "lence2@gmail.com", 93456712343)
        doctor = DoctorRep.Doctor_profile("001", "Dentistry", contact, 1)
        doctor = (doctor.schedule_appointment, 1, "doctor schedules appointment")
        doctor = DoctorRep.Doctor_profile.cancel_appointment("Dr joe", doctor)
        self.assertTrue(False, "cancelled appointment")
        self.assertNotIn("Jane Doe",doctor.appointment)

    def test_doctor_initialization(self):
        contact = ContactDetails("Dr grey", "lance", "lance2@gmail.com", 93456712343)
        doctor = DoctorRep.Doctor_profile("001", "Dentistry", contact, 1)
        self.assertEqual(doctor.doctor_id, "D001")
        self.assertEqual(doctor.specialization, "Dentistry")


    def test_invalid_appointment(self):
        contact = ContactDetails("Dr grey", "lance", "lance2@gmail.com", 93456712343)
        doctor = DoctorRep.Doctor_profile("001", "Dentistry", contact, 0)
        doctor = DoctorRep.Doctor_profile.invalidate_appointment
        self.assertEqual(doctor,"invalid appointment")



    # def test_doctor_attributes_are_set_correctly(self):
    #     contact = ContactDetails("firstname", "lastname", "abee23@gmail.com", 9187612343)
    #     doctor = DoctorRep.Doctor_profile(1, "general practitioner", contact)
    #
    #     attr1 = doctor.specialization
    #     attr2 = doctor.contact_details.email
    #     attr3 = doctor.doctor_id


    # def test_that_doctor_approves_patient_appointment(self):
    #     contact = ContactDetails("firstname", "lastname", "abee23@gmail.com", 9187612343)
    #     doctor = DoctorRep.Doctor_profile(1, "general practitioner", contact)
    #     appointment_date = datetime.date.today()
    #
    #     patient = Patient.request_appointment("Musa", appointment_date,'appointments')
    #     patient = Patient.get_patient_info(contact, appointment_date)
    #     Patient.assign_doctor(doctor.__init__("1234","general practitioner","contact_details"))
    #
    #     self.assertEqual(patient.doctor.doctor_id, 1)
    #     self.assertEqual(patient.doctor.specialization, "general practitioner")
    #     self.assertEqual(patient.doctor.contact_details.email, "abee23@gmail.com")

    #
    #     def test_doctor_string_representation(self):
    #         self.assertIn("Dr. Smith", str(self.doctor))
    #

    #     def test_treat_patient(self):
    #         treatment = self.doctor.treat_patient("John Doe")
    #         self.assertIsInstance(treatment, str)

