from flask import Blueprint, session, flash, redirect



logout = Blueprint("logout", __name__)


@logout.route("/logout")
def end_session():
    session.pop("username", None)
    session.pop("user_id", None)
    session.pop("user_type", None)
    
    flash("Logout successfully", "success")
    return redirect("/")