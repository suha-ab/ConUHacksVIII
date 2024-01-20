from flask import Flask, Blueprint, render_template
home = Blueprint('home', __name__)
@home.route('/')
def landing():
    return render_template('index.html', boolean=True)
