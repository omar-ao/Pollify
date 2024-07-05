#!/usr/bin/python3
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from models.user import User
from models import storage

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app():
    """Creates the application"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        """Load user by ID."""
        return storage.get(User, user_id)

    return app

