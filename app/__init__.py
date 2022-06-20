from flask import Flask
from flask_restful import Api
from app.error_handler import register_error_handlers


def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    api = Api(app, catch_all_404s=True)

    app.url_map.strict_slashes = False

    @app.route('/')
    def home():
        return f"Hello World this environment is: {settings_module}"

    register_error_handlers(app)

    return app

