from flask import Flask, make_response, abort


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/food_factory/hello')
    def hello():
        data = {"hello": "world"}
        return make_response(data, 200)

    @app.route('/food_factory/not_found')
    def not_found():
        abort(404)

    @app.route('/food_factory/unauthorized')
    def unauthorized():
        abort(403)

    @app.route('/food_factory/bad_request')
    def bad_request():
        abort(400)

    @app.route('/food_factory/app_error')
    def app_error():
        abort(500)

    return app
