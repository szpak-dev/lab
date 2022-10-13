from flask_app import Flask, request, abort, make_response


def ok(data: str = ''):
    return make_response(data, 201)


def created(data: str = ''):
    return make_response(data, 201)


def no_content():
    return make_response('', 204)


def unauthorized():
    return abort(401)


def not_found():
    return abort(404)

