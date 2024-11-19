from flask import Blueprint, render_template, redirect, request, session, flash
from app import db
from app.models import Link
from utilility import generate_random_string, generate_uniqueID

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
         customize_url = request.form.get("customize") # customise url name
         origin_url = request.form.get("url") # Destination link

         if customize_url: # if user provides a customize name
            existing = Link.query.filter_by(short_link=customize_url).first()


            if existing: # if customize name already exist in database
                 flash("Sorry, customize name has already been taken by another user", "warning")
                 return redirect("/")
            else:
                 # If customize name not found in database

                 new_link = Link(user_id=session.get("user_id"), origin_link=origin_url, short_link=customize_url)

                 db.session.add(new_link)
                 db.session.commit()

                 return redirect("/")

         else:
             # If user did not provide a customized name, generate unique random string for short url.

             while True:
                unique_value = generate_random_string()    
                existing = Link.query.filter_by(short_link=unique_value).first()

                if existing:
                    continue
                else:
                    break
            
            
             # If generated string doesn't exist in database

             if not session.get("username") and session.get("user_type") != "registered": # if it's not a registered user

                if not session.get("user_id"): # if anonymous user doesn't already have a user_id
                    session["user_id"] = f"anon_{generate_uniqueID()}" # generate an anonymous user_id
                    session["user_type"] = "anonymous"
                
                new_link = Link(anon_id=session.get("user_id"), origin_link=origin_url, short_link=unique_value) # Use anonymous id
            
             else:
                 # If it's a registered user
                 new_link = Link(user_id=session.get("user_id"), origin_link=origin_url, short_link=unique_value) # Use user_id

             
             # save to database
             db.session.add(new_link)
             db.session.commit()

             return redirect("/")

    elif session.get("username"):
        return render_template("home.html")
    else:
        return render_template("index.html")