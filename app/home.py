from flask import Flask, Blueprint
home = Blueprint('home', __name__)
@home.route('/')
def landing():
    return "home"