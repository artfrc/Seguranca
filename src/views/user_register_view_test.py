import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .user_register_view import UserRegisterView

class MockController:   
    def registry(self, username, password): #pylint: disable= W0613:unused-argument
        return { "anything": "anything" }

def test_handle():
    body = {
        'username': 'username',
        'password': 'password'
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    response = user_register_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body == { "data": { "anything": "anything" } }

def test_handle_with_validation_error():
    body = {
        'password': 'password'
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
        user_register_view.handle(request)


