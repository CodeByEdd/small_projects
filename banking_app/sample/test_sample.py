import unittest
from sample import account


class TestSample(unittest.TestCase):

    def test_checking_account_creation(self):
        user = account.CheckingAccount('Edd', 1)
        self.assertEqual(user.get_name(), 'Edd')

