import pytest

from atm.Atm import ATM
from atm.User import User
from atm.Account import Account
from atm.ChequeAccount import ChequeAccount
from atm.SavingsAccount import SavingsAccount


class TestATM:
    @pytest.fixture
    def atm_fixture(self):
        return ATM('data/UserInfo.txt', 'data/OpeningAccountsData.txt')

    def test_atm_creation(self, atm_fixture):
        assert type(atm_fixture.users) == type([])
        assert len(atm_fixture.users) == 3
        assert type(atm_fixture.accounts) == type ([])
        assert len(atm_fixture.accounts) == 5
        for user in atm_fixture.users:
            assert type(user) == User
        for account in atm_fixture.accounts:
            assert issubclass(type(account), Account)

    @pytest.fixture
    def user_fixture(self):
        return User("John", "Smith", "0403715629", "001")

    @pytest.fixture
    def account_option_fixture(self):
        return [
            SavingsAccount(123, 7840856, 55.00),
            ChequeAccount(123, 9256875, 100.00)
        ]

    def test_get_user_accounts(self, user_fixture, atm_fixture):
        user_accounts = atm_fixture.get_user_accounts
        assert type(user_accounts) == type ([])
        assert len(user_accounts) == 2
        for account in user_accounts:
            assert account.number in ["9264945", "7814135"]

    def test_get_account_options(self, atm_fixture, account_option_fixture):
        expected_string = """
    1 for 9264945 (Cheque)
    2 for 7814135 (Saving)"""

        options = atm_fixture.get_account_options(account_option_fixture)
        assert options == expected_string


if __name__ == '__main__':
    unittest.main()

