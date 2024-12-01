from abc import ABC, abstractmethod
from typing import Dict

class ILoginCreator(ABC):

    @abstractmethod
    def create(self, username: str, password: str) -> Dict:
        pass        