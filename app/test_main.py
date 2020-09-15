import pytest
import json

import main

# Fixtures are functions, which will run before each test function to which it is applied.
# Fixtures are used to feed some data to the tests such as database connections


@pytest.fixture
def app():
    """Creating an Flask app, returning its client"""

    app = main.create_app()
    app.debug = True
    return app.test_client()

# Testing route '/'


def test_hello(app):
    """Testing main route"""

    # Referencing app
    result = app.get("/")

    # Debugging
    print(result.data, result.status_code)

    # Tests
    assert result.status_code == 200
    assert b"Hello, I am a simple flask app!" in result.data


def test_register(app):
    """Testing registering of an app"""

    result = app.post("/register",
                    data=json.dumps({'login': 'mati', 'password': 'password'}),
                    content_type='application/json',)

    assert result.status_code == 200

    dict = {'login': 'mati', 'password': 'password'}
    assert dict == json.loads(str(result.data.decode("utf-8")))
