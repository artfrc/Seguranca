from src.controllers.interfaces.balance_editor import IBalanceEditor
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.errors.types.http_bad_request import HttpBadRequestError
from .interfaces.view_interface import ViewInterface

class BalanceEditorView(ViewInterface):
    def __init__(self, controller: IBalanceEditor):
        self.__controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        print("Headers:", request.headers)
        print("Body:", request.body)
        print("Params:", request.params)
        print("Token Infos:", request.token_infos)
        new_balance = request.body.get('new_balance')
        user_id = request.params.get('user_id')

        self.__validate_inputs(float(new_balance), user_id)

        response = self.__controller.edit_balance(user_id, new_balance)
        
        return HttpResponse(body={"data": response}, status_code=200)
            
    def __validate_inputs(self, new_balance: any, user_id: any):
        if(
            not new_balance
            or not user_id
            or not isinstance(new_balance, float)
        ):
            raise HttpBadRequestError('Invalid input')
    
        