"""The Netheret help desk web app.

create_app() builds the Flask app. Flask looks for a function with this
name when you run `flask --app helpdesk run`.
"""
from flask import Flask

from .extensions import db


def create_app():
    app = Flask(__name__)

    # SQLite keeps the whole database in one file. A relative path like this
    # one is put in the app's "instance" folder, which Git ignores.
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpdesk.db"

    # Tidy the HTML that templates produce: drop the blank lines left by
    # {% ... %} tags.
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    db.init_app(app)

    # Each part of the app is a blueprint: a group of pages in its own file.
    from . import main
    app.register_blueprint(main.bp)

    # Make any tables that do not exist yet. Importing models first tells
    # SQLAlchemy which tables there are.
    from . import models  # noqa: F401
    with app.app_context():
        db.create_all()

    return app
