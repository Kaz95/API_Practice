#! /usr/bin/python
from account_info import get_password


class Account:
    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role

    def authenticate(self):
        if get_password(self.name) != self.password:
            return 'Invalid password'
        else:
            return 'Welcome ' + self.name + ' !'
