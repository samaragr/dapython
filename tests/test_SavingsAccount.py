import pytest

from atm.SavingsAccount import SavingsAccount
class TestSavingsAccount:
    def test_savings_account_creation(self):
        number = "9264789"
        owner = 123
        balance = 100.00

        savings_account = SavingsAccount(owner, number, balance)
        assert savings_account.type == "Saving"
        assert savings_account.balance == balance
        assert savings_account.owner == owner
        assert savings_account.number == number