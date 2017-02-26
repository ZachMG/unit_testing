import unittest


class InvalidEmail:
    pass

class InvalidSocial:
    pass

class InvalidPassword:
    pass

class User:
    def __init__(self, username, email, ss, hash):
        self.username = username
        self.email = email
        self.ss = ss
        self.hash = hash

    def check_password(self, passwrd):
        return self.hash.eq(passwrd)

    def __str__(self):
        return self.username + ':\n' + \
               '    Email:' + str(self.email) + \
               '\n    Social: ' + str(self.ss)
