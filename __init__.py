from flask import Flask

def create_app():
    app = Flask(__name__)


    from .home import home
    from .queueTime import queueTime

    app.register_blueprint(home)
    app.register_blueprint(queueTime, url_prefix="/")

    return app