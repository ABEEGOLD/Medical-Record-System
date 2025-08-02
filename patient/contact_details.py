import re

class ContactDetails:
    def __init__(self, first_name: str, last_name: str, email: str, phone: str):
        if not self.is_valid_name(first_name):
            raise ValueError("Invalid first name - must be 2+ alphabetic characters")
        if not self.is_valid_name(last_name):
            raise ValueError("Invalid last name - must be 2+ alphabetic characters")
        if not self._is_valid_email(email):
            raise ValueError("Invalid email format")
        if not self._is_valid_phone(phone):
            raise ValueError("Invalid phone number - must be 10+ digits")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def is_valid_name(self, name: str) -> bool:
        return name.isalpha() and len(name) >= 2

    def _is_valid_email(self, email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]{3,}\.[a-zA-Z]{2,}'
        return re.match(pattern, email) is not None

    def _is_valid_phone(self, phone: str) -> bool:
        return phone.isdigit() and len(phone) >= 10

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"


