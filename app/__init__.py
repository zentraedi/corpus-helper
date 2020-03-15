from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True, static_folder='static')

# Load the default configuration
app.config.from_object('config.default')

# Load database
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

from app.mod_dashboard.controllers import entry_point
from app.mod_corpus.controllers import mod_corpus

# Register blueprint(s)
app.register_blueprint(entry_point, url_prefix='/')
app.register_blueprint(mod_corpus, url_prefix='/corpus')
