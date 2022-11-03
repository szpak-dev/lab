from flask import Request, make_response
from logger import logging

from sessions.adapters import request_interceptor


def _log_proxy_pass(req, res):
    logging.info('[ProxyPass] {} > {}'.format(req.path, res.status_code))


def proxy_pass_action(request: Request):
    res = request_interceptor.pass_request(request)
    _log_proxy_pass(request, res)
    text, headers, status_code = res.text, dict(res.headers), res.status_code

    flask_response = make_response(text, status_code, headers)
    flask_response.headers = headers

    return flask_response
