import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# Database URI
SQLALCHEMY_DATABASE_URI = 'postgres://USERNAME:PASSWORD@HOST:5432/DB_NAME'
SQLALCHEMY_TRACK_MODIFICATIONS = False