from src.controllers.interfaces.user_register import IUserRegister
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class UserRegisterView(ViewInterface):
    def __init__(self, controller: IUserRegister):
        self.__controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        username = request.body.get('username')
        password = request.body.get('password')
        self.__validate_inputs(username, password)

        response = self.__controller.registry(username, password)
        
        return HttpResponse(body={"data": response}, status_code=201)
            
    def __validate_inputs(self, username: any, password: any):
        if(
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ):
            raise Exception('Invalid input')
    
        