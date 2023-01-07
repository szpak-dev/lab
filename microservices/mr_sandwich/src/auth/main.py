from os import getenv

from fastapi import FastAPI, Request, Response
from uvicorn import run

from use_cases.create_user import Registration, create_user_action
from use_cases.login import Credentials, login_action
from use_cases.logout import logout_action
from use_cases.get_user import get_user_action, User
# from use_cases.proxy_pass import proxy_pass_action

app = FastAPI()


@app.post('/auth/users', status_code=201, tags=['User'])
def create_user(registration: Registration):
    create_user_action(registration)


@app.get('/auth/users', status_code=200, response_model=User, tags=['User'])
def me(request: Request):
    return get_user_action(request)


@app.post('/auth/login', status_code=201, tags=['Session'])
def login(response: Response, credentials: Credentials):
    login_action(credentials, response)


@app.delete('/auth/logout', status_code=204, tags=['Session'])
def logout(request: Request, response: Response):
    logout_action(request, response)


@app.route('/{full_path:path}', methods=['GET', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE'])
def proxy_pass(request: Request, full_path: str):
    pass
    # print(full_path)
    # return proxy_pass_action(request)


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
