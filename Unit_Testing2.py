from unit_testing import *
import unittest

class UnitTests(unittest.TestCase):
    def setUp(self):
        print('setUp()...')
        self.hash1 = Hash('1234')
        self.email1 = Email('zmg@verizon.net')

    def test(self):
        print('testing hash...')
        self.assertEqual(self.hash1, self.hash1) #failed
        self.assertNotEqual(self.hash1, Hash('123'))
        self.assertRaises(InvalidPassword, Hash, '1 ') #failed
        #self.assertEqual(length of Hash for two different passwords)
        print('testing email...')
        self.assertEqual(str(self.email1), 'zmg@verizon.net')
        self.assertRaises(InvalidEmail, Email, '@@') #failed
        self.assertRaises(InvalidEmail, Email, '@gmail.com') #failed
        print('testing social...')
        self.assertRaises(InvalidSocial, SS, '123456789')
        self.assertRaises(InvalidSocial, SS, '1234-567-89') #failed
        self.assertRaises(InvalidSocial, SS, '-') #failed
        self.assertRaises(InvalidSocial, SS, '1234-') #failed

    def tearDown(self):
        print('tearDown()...')
        del self.hash1
        del self.hash2
        del self.hash3
        del self.email1



