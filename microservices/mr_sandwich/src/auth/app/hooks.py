from app.user.adapters import UserAuthenticator


def on_authentication_started(username: str, password: str):
    UserAuthenticator().login(username, password)
