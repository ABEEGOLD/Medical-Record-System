import re

class ContactDetails:
    def __init__(self, first_name: str, last_name: str, email: str, phone: str):
        if not self._is_valid_name(first_name):
            raise ValueError("Invalid first name - must be 2+ alphabetic characters")
        if not self._is_valid_name(last_name):
            raise ValueError("Invalid last name - must be 2+ alphabetic characters")
        if not self._is_valid_email(email):
            raise ValueError("Invalid email format")
        if not self._is_valid_phone(phone):
            raise ValueError("Invalid phone number - must be 10+ digits")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email.lower().strip()
        self.phone = phone

    def _is_valid_name(self, name: str) -> bool:
        return name.isalpha() and len(name) >= 2

    def _is_valid_email(self, email: str) -> bool:
        email = email.lower().strip()

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            return False

        if email.count('@') != 1:
            return False

        local, domain = email.split('@')

        if len(local) < 1 or len(local) > 64:
            return False
        if local.startswith('.') or local.endswith('.'):
            return False
        if '..' in local:
            return False

        if len(domain) < 1 or len(domain) > 255:
            return False
        if domain.startswith('-') or domain.endswith('-'):
            return False
        if '..' in domain:
            return False

        valid_local_chars = set('abcdefghijklmnopqrstuvwxyz0123456789._%+-')
        valid_domain_chars = set('abcdefghijklmnopqrstuvwxyz0123456789.-')

        if not all(c in valid_local_chars for c in local):
            return False
        if not all(c in valid_domain_chars for c in domain):
            return False

        return True

    def _is_valid_phone(self, phone: str) -> bool:
        return phone.isdigit() and len(phone) >= 10

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"



