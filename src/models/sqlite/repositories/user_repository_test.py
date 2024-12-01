from unittest.mock import Mock
from src.models.sqlite.repositories.user_repository import UserRepository

class MockCursor:
    def __init__(self):
        self.execute = Mock()
        self.fetchone = Mock()

class MockConn:
    def __init__(self):
        self.cursor = Mock(return_value = MockCursor())
        self.commit = Mock()

def test_registry_user():

    username  = 'JohnDoe'
    password = '12345'

    mock_conn = MockConn()
    repo = UserRepository(mock_conn)
    repo.registry_user(username, password)

    cursor = mock_conn.cursor.return_value

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password, balance)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, 0)

    mock_conn.commit.assert_called_once()

def test_edit_balance():

    user_id  = 123
    new_balance = 100.50

    mock_conn = MockConn()
    repo = UserRepository(mock_conn)
    repo.edit_balance(user_id, new_balance)

    cursor = mock_conn.cursor.return_value

    assert "UPDATE users" in cursor.execute.call_args[0][0]
    assert "SET balance = ?" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (new_balance, user_id)

    mock_conn.commit.assert_called_once()

def test_get_user_by_username():

    username  = "JohnDoe"

    mock_conn = MockConn()
    repo = UserRepository(mock_conn)
    repo.get_user_by_username(username)

    cursor = mock_conn.cursor.return_value

    assert "SELECT id, username, password " in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username,)

    cursor.fetchone.assert_called_once()