import pytest
import json


# Testing route '/'
def test_hello(application):
    """Testing main route"""

    # Referencing app
    result = application.get("/")

    # Debugging
    print(result.data, result.status_code)
    print(type(application))

    # Tests
    assert result.status_code == 200
    assert b"Hello, I am a simple flask app!" in result.data


def test_register(application):
    """Testing registering of an app"""

    result = application.post("/register",
                    data=json.dumps({'login': 'mati', 'password': 'password'}),
                    content_type='application/json',)

    assert result.status_code == 200

    dict = {'login': 'mati', 'password': 'password'}
    assert dict == json.loads(str(result.data.decode("utf-8")))
