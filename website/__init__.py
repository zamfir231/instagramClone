#make imports
from flask import Flask
from .views import view

#principal function
def create_app():
    #initialize flask
    app = Flask(__name__)

    # -to be able to set up the actual pages
    app.register_blueprint(view, url_prefix="/")

    return app
