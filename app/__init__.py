from flask import Flask
from .config import Config
from flask_bootstrap import Bootstrap
from . import views, errors
from flask import Blueprint

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    bootstrap.init_app(app)

    return app

main = Blueprint('app', __name__)