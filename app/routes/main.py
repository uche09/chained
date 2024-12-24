from flask import Blueprint, render_template, redirect, request, session, flash, url_for
from app import db
from app.models import Link
from utilility import generate_random_string, generate_uniqueID
from datetime import datetime, timedelta

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        customize_url = request.form.get("customize") # customise url name
        origin_url = request.form.get("url") # Destination link
        
        if not origin_url:
            flash("Please provide the URL you want to shorten.", "error")
            return redirect("/")
        
        if customize_url: # if user provides a customize name
            existing = Link.query.filter_by(short_link=customize_url).first()
            
            
            if existing: # if customize name already exist in database
                 flash("Sorry, customize name has already been taken by another user", "warning")
                 return redirect("/")
            

            # If customize name not found in database
            new_link = Link(user_id=session.get("user_id"), origin_link=origin_url, short_link=customize_url)
            display_link = url_for("main.redirect_to_link", url=new_link.short_link, _external=True)

            db.session.add(new_link)
            db.session.commit()
            flash("Custom short link created successfully", "success")

            # Display newly generated link
            return render_template("home.html", display_link=display_link)
        

        # If user did not provide a customized name, generate unique random string for short url.
        while True:
            unique_value = generate_random_string()    
            existing = Link.query.filter_by(short_link=unique_value).first()

            if not existing:
                break
            
        
        # if it's not a registered user (is an anonymous user)
        if not session.get("username") and session.get("user_type") != "registered":
            
            # probably first time anonymous user
            if not session.get("user_id"):
                session["user_id"] = f"anon_{generate_uniqueID()}" # generate an anonymous user_id
                session["user_type"] = "anonymous"
            
            new_link = Link(anon_id=session.get("user_id"), origin_link=origin_url, short_link=unique_value) # Use anonymous id
            display_link = url_for("main.redirect_to_link", url=new_link.short_link, _external=True)
            
        else:
            # If it's a registered user
            new_link = Link(user_id=session.get("user_id"), origin_link=origin_url, short_link=unique_value) # Use user_id
            display_link = url_for("main.redirect_to_link", url=new_link.short_link, _external=True)

             
        # save to database
        db.session.add(new_link)
        db.session.commit()
        flash("Short link created successfully", "success")
        
        if session.get("user_type") == "registered":
            return render_template("home.html", display_link=display_link
                                   )
        # Display newly generated link
        return render_template("index.html", display_link=display_link)

    elif request.method == "GET":
        if session.get("username"):
            return render_template("home.html")
        else:
            return render_template("index.html")



@main.route("/<string:url>", methods=["GET"])
def redirect_to_link(url:str=""):
    '''
    Redirects the user based on the short URL provided.
    '''
    
    link = Link.query.filter_by(short_link=url).first()
    if link:
        print(link.origin_link)
        return redirect(link.origin_link)
    else:
        flash("This url is not recognized. \nGenerate a url.", "error")
        return redirect("/")