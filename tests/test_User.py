import pytest
from atm.User import User
class TestUser:

    @pytest.fixture
    def user_fixture(self):
        return User("John", "Doe", "0429810776", "001")

    @pytest.fixture
    def user_list_fixture(self):
        return [
            User("John", "Doe", "0429810776", "001"),
            User("Sally", "Jones", "0427763687", "123")]

    def test_user_creation(self):
        first_name = "John"
        last_name = "Doe"
        owner_id = 123
        mobile = "0420666789"

        user = User(first_name, last_name, mobile, owner_id)
        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.id == owner_id
        assert user.mobile == mobile

    def test_user_str(self, user_fixture):
        assert str(user_fixture) == "John Doe"

    def test_user_repr(self, user_list_fixture):
        assert str(user_list_fixture) == "[John Doe, Sally Jones]"
