import unittest
import os
import sys
testdir = os.path.dirname(__file__)
srcdir = '../src/atm'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from atm import ATM, Account, ChequeAccount, SavingsAccount, User

class TestATM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_atm = ATM()
        print('setupClass')
    def setUp(self):
        self.user_1 = User("John", "Doe", "0420666789", 123)
        self.account_1 = Account(123, "9264789", 100.00)

class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        self.assertEqual(TestATM.user_1.first_name, "John")
        self.assertEqual(TestATM.user_1.last_name, "Doe")
        self.assertEqual(TestATM.user_1.mobile, "0420666789")
        self.assertEqual(TestATM.user_1.id, 123)


class TestAccount(unittest.TestCase):
    def test_account_attributes(self):
        self.assertEqual(self.account_1.owner, 123)
        self.assertEqual(self.account_1.number, "9264789")
        self.assertEqual(self.account_1.balance, 100.00)

    def test_account_str_repr(self):
        self.assertEqual(str(self.account_1), "9264789 (None)")
        self.assertEqual(repr(self.account_1), "9264789 (None)")


class TestChequeAccount(unittest.TestCase):
    def test_cheque_account_type(self):
        cheque_account = ChequeAccount(123, "9264789", 100.00)
        self.assertEqual(cheque_account.type, "Cheque")


class TestSavingsAccount(unittest.TestCase):
    def test_savings_account_type(self):
        savings_account = SavingsAccount(123, "9264789", 100.00)
        self.assertEqual(savings_account.type, "Saving")

    @classmethod

    def tearDownClass(cls):
        print('tearDownClass')

if __name__ == '__main__':
    unittest.main()

