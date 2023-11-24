from flask import Flask
from flask_sqlalchemy import SQLAlchemy

API_KEY = 'bad466f22df141e2848115329232111'
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.sqlite3'
    db.init_app(app)

    from .main import home_blueprint
    app.register_blueprint(home_blueprint)

    with app.app_context():
        db.create_all()

    return app
