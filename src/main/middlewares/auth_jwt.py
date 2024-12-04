from flask import request
from src.drivers.jwt_handler import JwtHandler

def auth_jwt_verify():
    jwt_handler = JwtHandler()
    raw_token = request.headers.get('Authorization')
    user_id = request.headers.get('uid') # user id que o usuário envia

    if not raw_token or not user_id:
        raise Exception('Unauthorized')
    
    token = raw_token.split()[1] # Bearer <token>
    token_information = jwt_handler.decode_jwt_token(token)
    token_uid = token_information["user_id"] # checar se o user id que o usuário envia é o mesmo que está no token

    if user_id and token_uid and (int(token_uid) == int(user_id)):
        return token_information
    
    raise Exception('User unauthorized')

