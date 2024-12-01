from abc import ABC, abstractmethod
from typing import Tuple

class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def registry_user(self, username: str, password: str): pass

    @abstractmethod
    def edit_balance(self, user_id: int, new_balance: float): pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> Tuple[int, str, str]:
        pass