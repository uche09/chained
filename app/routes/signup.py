from flask import Blueprint, render_template, request, session, flash, redirect
from werkzeug.security import generate_password_hash
from app.models import User
from utilility import is_secure
from app import db


signup = Blueprint("signup", __name__)

@signup.route("/signup", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        

        if not (email and username and password):
            flash("Please provide all inputs.", "error")
            return redirect("/auth/signup")
        
        users = User.query.filter_by(username=username).all()

        # checks if username already exist in database
        if users:
            flash("Username has alrdady been taked..\nTry something else.", "error")
            return redirect('/auth/signup')
        
        # Verify email address
        elif not (".com" in email) and not ('@' in email):
            flash("Invalid Email", "error")
            return redirect("/auth/signup")
        
        if not is_secure(password):
            flash("Password is to weak: password should be at least 8 characters long,\n have at least one uppercase letter,\n"
                  " one lowercase letter,\n one digit and one symbol", "error")
            return redirect("/auth/signup")
        

        # Save new user details to database
        new_user = User(email=email, username=username, password_hash=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()

        # Login new user
        session["username"] = username

        flash("Account created successfully!", "success")
        return redirect("/")
        
    else:
        return render_template("signup.html")