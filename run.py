"""Create an application instance."""
from flask.helpers import get_debug_flag


from app.app import create_app
from app.settings import DevConfiguration, ProdConfiguration


# Get whether debug mode should be enabled for the app, indicated
# by the :envvar:`FLASK_DEBUG` environment variable.

# Getting configuration as python object
CONFIG = DevConfiguration if get_debug_flag() else ProdConfiguration

app = create_app(CONFIG)
app.run()