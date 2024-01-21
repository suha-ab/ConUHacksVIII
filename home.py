from flask import Flask, Blueprint, render_template, request, redirect
home = Blueprint('home', __name__)
@home.route('/')
def landing():
    if request.method == 'GET':
        return render_template('index.html', boolean=True)
    if request.method == 'POST':
        return redirect()
