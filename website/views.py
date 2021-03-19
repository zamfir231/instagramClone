#import what we need
from flask import Blueprint, render_template

#make view variable/Blueprint
view = Blueprint("views", __name__)

#set up urls
@view.route('/')
def home():
    return render_template('index.html')
