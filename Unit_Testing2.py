from unit_testing import *
import unittest

class UnitTests(unittest.TestCase):
    def setUp(self):
        print('setUp()...')
        self.hash1 = Hash('1234')
        self.hash2 = Hash('1234')
        self.hash3 = Hash('123')
        self.email1 = Email('P@V')

    def test(self):
        print('testing hash...')
        self.assertEqual(self.hash1, self.hash2) #failed
        self.assertNotEqual(self.hash1, self.hash3)
        self.assertRaises(InvalidPassword, Hash, '1')
        print('testing email...')
        self.assertEqual(str(self.email1), 'P@V')
        self.assertRaises(InvalidEmail, Email, 'thing')
        self.assertRaises(InvalidEmail, Email, '@gmail.com') #failed
        print('testing social...')
        self.assertRaises(InvalidSocial, SS, '123456789')
        self.assertRaises(InvalidSocial, SS, '1234-567-89') #failed
        self.assertRaises(InvalidSocial, SS, '-') #failed
        self.assertRaises(InvalidSocial, SS, '1234')

    def tearDown(self):
        print('tearDown()...')
        del self.hash1
        del self.hash2
        del self.hash3
        del self.email1



