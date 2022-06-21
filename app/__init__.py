from flask import Flask
from flask_restful import Api
from app.error_handler import register_error_handlers
from .resources.berry import BerryStatistics


def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    api = Api(app, catch_all_404s=True)
    api.add_resource(BerryStatistics, '/allBerryStats')

    app.url_map.strict_slashes = False

    register_error_handlers(app)

    return app

