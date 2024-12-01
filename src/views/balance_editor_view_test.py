import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .balance_editor_view import BalanceEditorView

class MockController:
    def edit_balance(self, user_id, new_balance):
        return {"user_id": user_id, "new_balance": new_balance}  

def test_handle():
    body = {
        'new_balance': 100.0
    }
    params = {'user_id': 1}

    request = HttpRequest(body=body, params=params)
    balance_editor_view = BalanceEditorView(MockController())
    response = balance_editor_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body == {"data": {"user_id": 1, "new_balance": 100.0}}

def test_handle_with_validation_error():
    body = {
        'new_balance': '100.0'
    }
    params = {'user_id': 1}

    request = HttpRequest(body=body, params=params)
    balance_editor_view = BalanceEditorView(MockController())

    with pytest.raises(Exception):
        balance_editor_view.handle(request)
