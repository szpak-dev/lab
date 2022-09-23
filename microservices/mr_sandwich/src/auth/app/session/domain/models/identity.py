from app.session.domain.models.jwt import Jwt
from app.session.domain.models.session_id import SessionId


class Identity:
    def __init__(self, session_id=None, jwt=None):
        if session_id is None and jwt is None:
            raise RuntimeError('No Identity found')

        self._session_id = session_id
        self._jwt = jwt

    def requested_from_internet(self):
        return type(self._session_id) is SessionId

    def requested_from_subnet(self):
        return type(self._jwt) is Jwt

    def value(self) -> str:
        if self._session_id is not None:
            return self._session_id.id

        return self._jwt.jwt
