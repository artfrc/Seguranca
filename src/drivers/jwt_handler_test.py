from .jwt_handler import JwtHandler

def test_jwt_handler():
    jwt_handler = JwtHandler()
    body = {
        "username": "test_user",
        "anything": "anything",
        "blablabla": ""
    }

    token = jwt_handler.create_jwt_token(body)
    info_token = jwt_handler.decode_jwt_token(token)

    assert token is not None
    assert isinstance(token, str)
    assert info_token['username'] == body['username']