from flask import Flask
from . import views

main = Flask('main', __name__, static_folder='static', template_folder='templates')

