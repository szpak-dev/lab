from app.session.adapters import session_repository, jwt_repository
from app.session.domain.value_objects import Identity
from app.session.domain.errors import SessionNotFound


def assert_valid_identity(identity: Identity):
    value = identity.value()

    if identity.requested_from_internet():
        return session_repository.assert_exists(value)

    if identity.requested_from_subnet():
        return jwt_repository.assert_is_ours(value)

    raise SessionNotFound
