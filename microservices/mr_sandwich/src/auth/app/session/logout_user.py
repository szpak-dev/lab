from flask import make_response


class LogoutUser:
    def run(self, user_id: str):
        response = make_response('', 204)
        response.delete_cookie('session_id')
        return response
