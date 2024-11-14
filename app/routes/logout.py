from flask import Blueprint, session, flash, redirect



logout = Blueprint("logout", __name__)


@logout.route("/logout")
def end_session():
    session.pop("username")
    session.pop("user_id")
    
    flash("Logout successfully", "success")
    return redirect("/")