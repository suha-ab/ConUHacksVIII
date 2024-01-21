from flask import Flask, Blueprint, render_template
queueTime = Blueprint('queueTime', __name__)
@queueTime.route('/queueTime')
def dateAndTime():
    return render_template('queueDateAndTime.html', boolean=True)