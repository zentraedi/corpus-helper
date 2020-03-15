from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.mod_dashboard.controllers import entry_point


app = Flask(__name__, instance_relative_config=True, static_folder='static')

# Load the default configuration
app.config.from_object('config.default')

# Load database
# db = SQLAlchemy(app)

# Register blueprint(s)
app.register_blueprint(entry_point, url_prefix='/')
