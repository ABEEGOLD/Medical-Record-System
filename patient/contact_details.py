class ContactDetails:
    def __init__(self, first_name:str, last_name:str, email:str, phone_number:int):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number


    def __repr__(self):
        return f"First_name: {self.first_name} , Last_name: {self.last_name} , Email: <{self.email}> Phone: {self.phone_number}"

    @property
    def get_first_name(self):
        return self.first_name
    @get_first_name.setter
    def get_first_name(self, value):
        if type(value) == str:
            self.first_name = value
        else:
            raise TypeError('First name must be a string')
    @property
    def get_last_name(self):
        return self.last_name
    @get_last_name.setter
    def get_last_name(self, value):
        if type(value) == str:
            self.last_name = value
        else:
            raise TypeError('Last name must be a string')
    @property
    def get_email(self):
        return self.email
    @get_email.setter
    def get_email(self, value):
        if type(value) == str:
            self.email = value
        else:
            raise TypeError('Email must be a string')
    @property
    def get_phone_number(self):
        return self.phone_number
    @get_phone_number.setter
    def get_phone_number(self, value):
        if type(value) == int:
            self.phone_number = value
        else:
            raise TypeError('Phone number must be a number')
    @property
    def get_age(self):
        return self.age
    @get_age.setter
    def get_age(self, value):
        if type(value) == int:
            self.age = value
        else:
            raise TypeError('Age must be a number')