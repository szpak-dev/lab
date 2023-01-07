from os import getenv

from fastapi import FastAPI, HTTPException, Response
from uvicorn import run

from domain.errors import SessionError
from domain.errors import UserError
from use_cases.create_user import Registration, create_user_action
from use_cases.login import Credentials, login_action

app = FastAPI()


@app.post('/auth/users', status_code=201, tags=['Users'])
def create_user(registration: Registration):
    create_user_action(registration)


@app.post('/auth/login', status_code=201, tags=['Session'])
def login(response: Response, credentials: Credentials):
    try:
        login_action(credentials, response)
    except (UserError, SessionError):
        raise HTTPException(status_code=401, detail='Invalid credentials')


# @app.delete('/auth/logout', status_code=204, tags=['Session'])
# def logout():
#     pass
#
#
# @app.get('/auth/users', status_code=200, tags=['User'])
# def me():
#     pass
#
#
# def proxy_pass(path):
#     pass


if __name__ == "__main__":
    run(
        app,
        host="0.0.0.0",
        port=80,
        log_level=getenv('WSGI_LOG_LEVEL', 'debug'),
        proxy_headers=True,
        workers=1,
        access_log=False,
    )
