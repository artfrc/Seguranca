from typing import Dict, Tuple
from src.models.interfaces.user_repository import UserRepositoryInterface
from src.drivers.jwt_handler import JwtHandler
from src.drivers.password_handler import PasswordHandler

class LoginCreator:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository
        self.__jwt_handler = JwtHandler()
        self.__password_handler = PasswordHandler()

    def create(self, username: str, password: str) -> Dict:
        user = self.find_user(username)
        user_id = user[0]
        hashed_password = user[2]
        self.__verify_password(password, hashed_password)
        token = self.create_jwt_token(user_id)
            
        return self.__format_response(username, token)

    def find_user(self, username: str) -> Tuple[int, str, str]:
        repo = self.__user_repository   
        user = repo.get_user_by_username(username)
        if not user:
            raise Exception("User not found") #pylint: disable=W0719, broad-exception-raised
        return  user
    
    def __verify_password(self, password: str, hashed_password: str):
        is_password_correct =  self.__password_handler.check_password(password, hashed_password)
        if not is_password_correct:
            raise Exception("Wrong password") #pylint: disable=W0719, broad-exception-raised
        
    def create_jwt_token(self, user_id: int) -> str:
        pay_load = {
            "user_id": user_id
        }
        token = self.__jwt_handler.create_jwt_token(pay_load)

        return token
    
    def __format_response(self,username: str, token: str) -> Dict:
        return {
            "access": True,
            "username": username,
            "authorization": token
        }
        