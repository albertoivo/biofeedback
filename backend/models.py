from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

# -------------------------------------------------------------------------- #
# Config & Flask-Migrate.
# -------------------------------------------------------------------------- #


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# -------------------------------------------------------------------------- #
# Models.
# -------------------------------------------------------------------------- #


class User(db.Model):
    """User Entity"""

    email = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
