from abc import ABC, abstractmethod
from typing import Dict

class IUserRegister(ABC):

    @abstractmethod
    def registry(self, username: str, password: str) -> Dict:
        pass
