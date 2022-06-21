import os
from flask import Flask, render_template, url_for
from flask_restful import Api
from app.error_handler import register_error_handlers
from .resources.berry import BerryStatistics


def create_app(settings_module):
    app = Flask(__name__, static_folder=os.path.abspath("static"))
    app.config.from_object(settings_module)

    api = Api(app, catch_all_404s=True)
    api.add_resource(BerryStatistics, '/allBerryStats')

    app.url_map.strict_slashes = False
    @app.route('/')
    def home():
        filename = url_for('static', filename="images/histogram.png")
        return render_template('index.html', hist_image=filename)

    register_error_handlers(app)

    return app

