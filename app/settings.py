"""Configuration of application."""

import os

class DevConfiguration(object):
    """This class consists app constants for Development environment."""

    PORT = 5000
    HOST = '0.0.0.0'

class ProdConfiguration(object):
    """This class consists app constants for Production environment."""

    PORT = 5001
    HOST = '0.0.0.0'

class TestConfiguration(object):
    """This class consists app constants for Production environment."""

    PORT = 5002
    HOST = '0.0.0.0'
