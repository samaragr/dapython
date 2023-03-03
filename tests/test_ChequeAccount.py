import pytest

from atm.ChequeAccount import ChequeAccount
class TestChequeAccount:
    def test_cheque_account_creation(self):
        number = "9264789"
        owner = 123
        balance = 100.00

        savings_account = ChequeAccount(owner, number, balance)
        assert savings_account.type == "Cheque"
        assert savings_account.balance == balance
        assert savings_account.owner == owner
        assert savings_account.number == number