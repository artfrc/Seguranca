from src.controllers.interfaces.login_creator import ILoginCreator
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.errors.types.http_bad_request import HttpBadRequestError
from .interfaces.view_interface import ViewInterface

class LoginCreatorView(ViewInterface):
    def __init__(self, controller: ILoginCreator):
        self.__controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        username = request.body.get('username')
        password = request.body.get('password')
        self.__validate_inputs(username, password)

        response = self.__controller.create(username, password)
        
        return HttpResponse(body={"data": response}, status_code=200)
            
    def __validate_inputs(self, username: any, password: any):
        if(
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ):
            raise HttpBadRequestError('Invalid input')
    
        