import os

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY') or 'not-the-droid-youre-looking-for'

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLSERVER = {
    'user': 'pr_test',
    'pw': 'test',
    'db': 'pr_test',
    'host': '131.94.128.214',
    'port': '5432',
}

SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ECHO = True
