from src.controllers.interfaces.balance_editor import IBalanceEditor
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class BalanceEditorView(ViewInterface):
    def __init__(self, controller: IBalanceEditor):
        self.__controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        new_balance = request.body.get('new_balance')
        user_id = request.params.get('user_id')
        self.__validate_inputs(new_balance, user_id)

        response = self.__controller.edit_balance(user_id, new_balance)
        
        return HttpResponse(body={"data": response}, status_code=200)
            
    def __validate_inputs(self, new_balance: any, user_id: any):
        if(
            not new_balance
            or not user_id
            or not isinstance(new_balance, float)
            or not isinstance(user_id, int)
        ):
            raise Exception('Invalid input')
    
        