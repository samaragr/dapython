import pytest
from atm.Account import Account
class TestAccount:
    @pytest.fixture
    def account_fixture(self):
        return Account(123, "9264789", 100.00)

    @pytest.fixture
    def account_list_fixture(self):
        return [
            Account(123, "9264789", 100.00),
            Account(456, "1234568", 50.00)
        ]
    def test_account_creation(self, account_fixture):
        assert account_fixture.owner == 123
        assert account_fixture.number == "9264789"
        assert account_fixture.balance == 100.00

    def test_account_str(self, account_fixture):
        assert str(account_fixture) == "9264789 (Unspecified)"

    def test_account_repr(self, account_list_fixture):
        assert str(account_list_fixture) == "[9264789 (Unspecified), 1234568 (Unspecified)]"
