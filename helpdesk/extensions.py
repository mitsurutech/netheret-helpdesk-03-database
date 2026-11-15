"""Objects shared by the whole app.

db is made here, not in __init__.py, so that models.py can import it
without importing the whole app (that would be a circular import).
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
