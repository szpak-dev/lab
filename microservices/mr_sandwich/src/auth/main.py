from fastapi import FastAPI, Request, Response

from use_cases.create_user import Registration, create_user_action
from use_cases.login import Credentials, login_action
from use_cases.logout import logout_action
from use_cases.get_user import get_user_action, User
from use_cases.proxy_pass import proxy_pass_action

methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
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


@app.api_route('/web_store_cart/{full_path:path}', methods=methods)
@app.api_route('/food_factory/{full_path:path}', methods=methods)
def proxy_pass(full_path: str, request: Request):
    print(str(request.scope))
    return proxy_pass_action(request)