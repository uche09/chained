from flask import Blueprint, render_template, redirect
from app import db
# from app.models

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")