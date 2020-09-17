import pytest


from app.app import create_app
from app.settings import DevConfiguration, TestConfiguration

# Fixtures are functions, which will run before each test function to which it is applied.
# Fixtures are used to feed some data to the tests such as database connections


@pytest.fixture
def application():
    """Creating an Flask app, returning its client"""

    app = create_app(TestConfiguration)
    app.debug = True
    return app.test_client()
