from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .login_creator_view import LoginCreatorView

class MockController:
    def create(self, useranme:str, password:str): #pylint: disable= W0613:unused-argument
        return { "anything": "anything" }
    
def test_handle():
    body = {
        "username": "username",
        "password": "password"
    }
    request = HttpRequest(body=body)
    controller = MockController()
    login_creator_view = LoginCreatorView(controller)

    response = login_creator_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body == { "data": { "anything": "anything" } }



