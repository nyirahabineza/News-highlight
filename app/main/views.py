from flask import render_template,request,redirect,url_for

from . import main
from ..requests import get_news,get_news,search_news

from .forms import ReviewForm
from ..models import Review

# Views
@main.route('/')
def index():

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
