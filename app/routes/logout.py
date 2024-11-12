from flask import Blueprint, session, flash, redirect



logout = Blueprint("logout", __name__)


@logout.route("/logout")
def end_session():
    session.pop("username")
    
    flash("Logout successfully", "success")
    return redirect("/")