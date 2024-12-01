from abc import ABC, abstractmethod
from typing import Dict

class IBalanceEditor(ABC):

    @abstractmethod
    def edit_balance(self, user_id: int, new_balance: float) -> Dict:
        pass        