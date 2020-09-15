from flask import Flask, request


def create_app():

    app = Flask(__name__)

    @app.route('/')
    def hello() -> str:
        return 'Hello, I am a simple flask app!'

    @app.route('/register', methods=['POST'])
    def register() -> dict:
        """Registering new users"""

        json = request.get_json()
        login = json['login']
        password = json['password']

        return {"login": login, "password": password}

    return app


if __name__ == "__main__":
    port = 8000
    app = create_app()
    app.run(host="0.0.0.0", port=port)

# curl -H "Content-Type: application/json" -X POST -d '{"login":"mateusz"}' http://127.0.0.1:5000/register
