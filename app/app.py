"""This module contains flask app and its routes"""

from flask import Flask, request
from app.settings import DevConfiguration, ProdConfiguration


def create_app(configuration_py_file) -> Flask:
    """This function is initiating flask application. Consists route paths"""

    app = Flask(__name__)
    app.config.from_object(configuration_py_file)

    @app.route('/')
    def hello() -> str:
        """Hello world method"""
        return 'Hello, I am a simple flask app!'

    @app.route('/register', methods=['POST'])
    def register() -> dict:
        """Registering new users"""

        json = request.get_json()
        login = json['login']
        password = json['password']

        return {"login": login, "password": password}

    return app
