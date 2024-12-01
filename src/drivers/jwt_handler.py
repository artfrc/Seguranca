from typing import Dict
from datetime import datetime, timedelta, timezone
import jwt
from src.configs.jwt_configs import jwt_infos

class JwtHandler:
    def create_jwt_token(self, body: Dict = {}) -> str: #pylint: disable= W0102, dangerous-default-value
        token = jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(minutes=int(jwt_infos['JWT_HOURS'])),
                **body
            },
            key=jwt_infos['KEY'],
            algorithm=jwt_infos['ALGORITHM']
        )

        return token
    
    def decode_jwt_token(self, token: str) -> Dict:
        token_info = jwt.decode(
            token,
            key=jwt_infos['KEY'],
            algorithms=jwt_infos['ALGORITHM']
        )

        return token_info
