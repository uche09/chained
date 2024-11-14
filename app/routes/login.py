from flask import Blueprint, render_template, request, session, flash, redirect
from werkzeug.security import check_password_hash
from app.models import User
from app import db


login = Blueprint("login", __name__)

@login.route("/login", methods=["GET", "POST"])
def logger():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Please input all feilds", "error")
            return redirect("/auth/login")
        
        # query database if username exist
        user = User.query.filter_by(username=username).first()
        
        # If username does not exist in database
        if not user:
            flash("Incorrect username or password", "error")
            return redirect("/auth/login")
        
        # validate if password is match
        if not check_password_hash(user.password_hash, password):
            flash("Incorrect username or password", "error")
            return redirect("/auth/login")
        
        # log user in via session
        session["username"] = user.username
        session["user_id"] = user.id
        
        flash("logged in successfully", "success")
        return redirect("/")

    else:
        return render_template("login.html")