import datetime

from patient.contact_details import ContactDetails

from patient.patient import Patient

from Appointment.appointment import Appointment

from Doctor.doctor_go.doctor_rep import  DoctorProfile


class ClinicAdmin:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def register_patient(self, patient: Patient):
        self.patients.append(patient)

    def register_doctor(self, doctor: DoctorProfile):
        self.doctors.append(doctor)

    def search_patient_by_id(self, patient_id:int):
        for p in self.patients:
            if p.id == patient_id:
                return p
        return None
    def search_doctor_by_id(self, doctor_id:int):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None

    def search_appointment_by_id(self, appointment_id: int):
        for appt in self.appointments:
            if appt.appointment_id  == appointment_id:
                return appt
        return None
    def book_appointment(self, appointment_id, patient_id, doctor_id,reason,date=datetime.date.today()):
        patient = self.search_patient_by_id(patient_id)
        doctor = self.search_doctor_by_id(doctor_id)
        if not patient or not doctor:
            raise ValueError("Patient or doctor not found")
        appointment = Appointment(appointment_id, patient, doctor,reason,date=datetime.date(2025,11,1))
        self.appointments.append(appointment)
        patient.appointments.append(appointment)
        return appointment

    def cancel_appointment(self, appointment_id):
        for appts in self.appointments:
            if appts.appointment_id == appointment_id:
                appts.cancel()
            return True
        return False

    def get_all_patient_summaries(self):
        for patient in self.patients:
            print(patient)

    def patients_by_doctor(self, doctor_id: int):
        return list({appt.patient for appt in self.appointments if appt.doctor.id == doctor_id})

    def generate_appointment_report(self):
        for appt in self.appointments:
            print(str(appt))

    def print_summary(self, doctor_id: int):
        doctor = self.search_doctor_by_id(doctor_id)
        if not doctor:
            print("Doctor not found.")
            return
        print(f"Doctor: {doctor.contact_details.first_name} {doctor.contact_details.last_name} ({doctor.specialization})")
        appointments = [appt for appt in self.appointments if appt.doctor.doctor_id == doctor_id]
        for appt in appointments:
            patient = appt.patient
            print(f"{appt.doctor}  {appt.date}  {appt.appointment_is_booked_status}  Patient: {patient.contact_details.first_name} {patient.contact_details.last_name}")



contact_patient1 = ContactDetails("rasaq", "ajape", "rasaq@email.com", 1234567890)
contact_patient2 = ContactDetails("John", "okafor", "john@email.com", 9876543210)
contact_doctor1 = ContactDetails("sikiru", "ayinla", "sikiru@email.com", 5551234567)
contact_doctor2 = ContactDetails("chibuzor", "emmanuel", "chibuzor@email.com", 5559876543)

# Create some doctors
doctor1 = DoctorProfile(1, "gynecologist", contact_doctor1)
doctor2 = DoctorProfile(2, "Pediatrician", contact_doctor2)

# Create some patients
patient1 = Patient(101, contact_patient1, datetime.date(1985, 5, 15))
patient1.medical_history.extend([
    "Diagnosed with hypertension in 2018",
    "Allergic to penicillin",
    "Underwent appendectomy in 2010"
])
patient2 = Patient(102, contact_patient2 , datetime.date(1990, 8, 22))
patient2.medical_history.extend([
    "Asthma since childhood",
    "Broken arm in 2015",
    "Seasonal allergies"
])

patient1.medical_note.append("Blood pressure slightly elevated at last visit (140/90)")
patient2.medical_note.append("Asthma well-controlled with current medication")

admin = ClinicAdmin()
admin.register_doctor(doctor1)
admin.register_doctor(doctor2)
admin.register_patient(patient1)
admin.register_patient(patient2)

admin.book_appointment(1001, 101, 1,"Heart checkup", datetime.date(2025, 11, 15))
admin.book_appointment(1002, 102, 1,"Chest pain", datetime.date(2025, 11, 16))
admin.book_appointment(1003, 101, 2, "Child wellness visit",datetime.date(2025, 11, 17))
admin.book_appointment(1004, 102, 2,"Vaccination",datetime.date(2025, 11, 18))

admin.cancel_appointment(1002)

appointment_found = admin.search_appointment_by_id(1003)
if appointment_found:
    appointment_found.appointments_complete()

    def print_patient_details(patient):
        print(f"\nPatient ID: {patient.id}")
        print(f"Name: {patient.contact_details.first_name} {patient.contact_details.last_name}")
        print(f"DOB: {datetime.date(1990,11,5)}")
        print(f"Email: {patient.contact_details.email}")
        print(f"Phone: {patient.contact_details.phone_number}")

        print("\nMedical History:")
        for m_history, entry in enumerate(patient.medical_history, 1):
            print(f"{m_history}. {entry}")

        print("\nMedical Notes:")
        for m_note, note in enumerate(patient.medical_note, 1):
            print(f"{m_note}. {note}")

        print("\nUpcoming Appointments:")
        for appt in patient.appointments:
            if appt.appointment_is_booked_status == "Scheduled":
                print(f"- {appt.date}: With Dr. {appt.doctor.contact_details.last_name} ({appt.doctor.specialization}) for {appt.reason}")
        print(
            f"- {appt.date}: With Dr. {appt.doctor.contact_details.last_name} ({appt.doctor.specialization}) for {appt.appointment_reason}")


print("=== PATIENT MEDICAL RECORDS ===")
print_patient_details(patient1)
print_patient_details(patient2)

print("\n=== DOCTOR'S APPOINTMENTS ===")
admin.print_summary(1)


