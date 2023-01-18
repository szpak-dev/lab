import httpx
from fastapi import Request, HTTPException

from domain.errors import SessionNotFound, JwtClaimsNotFound
from domain.services import extract_session_id, encode_jwt
from adapters import session_repository, jwt_claims_repository
from shared.logger import logging


def _log_proxy_pass(req, res):
    logging.info('[ProxyPass] {} > {}'.format(req.file, res.status_code))


async def proxy_pass_action(request: Request):
    try:
        session_id = extract_session_id(request)
        session = session_repository.get_by_id(session_id)

        jwt_claims = jwt_claims_repository.get_by_session_id(session.id)
        encoded_jwt = encode_jwt(jwt_claims)
    except (SessionNotFound, JwtClaimsNotFound) as e:
        raise HTTPException(status_code=401, detail=str(e))

    content = await request.body()

    headers = dict(request.headers.items())
    headers['Authorization'] = 'Bearer {}'.format(encoded_jwt)

    with httpx.Client() as client:
        try:
            return client.request(
                method=request.method,
                url=str(request.url),
                content=content,
                headers=headers,
                params=request.query_params,
            )
        except httpx.HTTPError as e:
            print(str(e))
