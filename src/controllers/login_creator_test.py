from src.drivers.password_handler import PasswordHandler
from .login_creator import LoginCreator
import pytest

USERNAME_GLOBAL = "john"
PASSWORD = "123456"
hashed_password = PasswordHandler().encrypt_password(PASSWORD)

class MockUserRepository:
    def get_user_by_username(self, username):
        return (10, username, hashed_password)

def test_create():
    repo = LoginCreator(MockUserRepository())
    response = repo.create(USERNAME_GLOBAL, PASSWORD)

    assert response["access"] 
    assert response["username"] == USERNAME_GLOBAL
    assert "authorization" is not None

def test_create_with_wrong_password():
    repo = LoginCreator(MockUserRepository())

    with pytest.raises(Exception):
        repo.create(USERNAME_GLOBAL, 'PASSWORD')