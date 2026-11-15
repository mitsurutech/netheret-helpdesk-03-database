"""General pages that do not belong to one feature."""
from flask import Blueprint, render_template

from .extensions import db
from .models import Article, Company, Job, Ticket, User

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    # Count the rows in each table, to show the database is working.
    counts = {
        "companies": db.session.query(Company).count(),
        "users": db.session.query(User).count(),
        "support requests": db.session.query(Ticket).count(),
        "jobs": db.session.query(Job).count(),
        "articles": db.session.query(Article).count(),
    }
    return render_template("home.html", counts=counts)
