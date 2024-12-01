from .password_handler import PasswordHandler

def test_encrypt():
    my_pass = "123Rocket"
    password_handler = PasswordHandler()
    hashed_password = password_handler.encrypt_password(my_pass)

    pass_checked = password_handler.check_password(my_pass, hashed_password)

    assert pass_checked