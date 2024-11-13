from flask import Blueprint, render_template, redirect, request, session
from app import db
# from app.models

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pass
    elif session.get("username"):
        return render_template("home.html")
    else:
        return render_template("index.html")