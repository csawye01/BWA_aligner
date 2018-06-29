from flask import Flask, render_template
from . import views
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

app.config['SECRET_KEY'] = 'F34TF$($e34D'
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500