from typing import Dict
from datetime import datetime, timedelta, timezone
import jwt

class JwtHandler:
    def create_jwt_token(self, body: Dict = {}) -> str: #pylint: disable= W0102, dangerous-default-value
        token = jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(minutes=1),
                **body
            },
            key='my_secret_key',
            algorithm='HS256'
        )

        return token
    
    def decode_jwt_token(self, token: str) -> Dict:
        token_info = jwt.decode(
            token,
            key='my_secret_key',
            algorithms=['HS256']
        )

        return token_info
