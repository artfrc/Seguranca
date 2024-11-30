from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from .user_repository import UserRepository

def test_repository():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)

    username = 'JohnDoe'
    password = "123Rocket!"

    repo.registry_user(username, password)
    user = repo.get_user_by_username(username)

    print()
    print(user)
    repo.edit_balance(user[0], 1000)
    user = repo.get_user_by_username(username)
    print(user)