from .balance_editor import BalanceEditor

class MockUserRepository:
    def __init__(self):
        self.edit_balance_attributes = {
            "user_id": 1,
            "balance": 1000
        }

    def edit_balance(self, user_id: int, new_balance: float):
        self.edit_balance_attributes["user_id"] = user_id
        self.edit_balance_attributes["balance"] -= new_balance

def test_edit_balance():
    repo = MockUserRepository()
    controller = BalanceEditor(repo)
    response = controller.edit_balance(
        repo.edit_balance_attributes["user_id"], 
        500)

    assert response["type"] == "User"
    assert response["count"] == 1
    assert response["data"]["new_balance"] == 500