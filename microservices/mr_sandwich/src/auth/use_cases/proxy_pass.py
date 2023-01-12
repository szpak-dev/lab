import httpx
from fastapi import Request, Response

from domain.services import extract_session_id, encode_jwt
from adapters import session_repository, jwt_claims_repository
from shared.logger import logging


def _log_proxy_pass(req, res):
    logging.info('[ProxyPass] {} > {}'.format(req.file, res.status_code))


def proxy_pass_action(request: Request):
    # pass
    session_id = extract_session_id(request)
    session = session_repository.get_by_id(session_id)

    jwt_claims = jwt_claims_repository.get_by_session_id(session.id)
    print(jwt_claims)
    encoded_jwt = encode_jwt(jwt_claims)
    #
    # return httpx.request(
    #     method=request.method,
    #     url=request.headers.get('Host'),
    #     headers=request.headers,
    #     params=request.query_params,
    # )
