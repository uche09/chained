from flask import Blueprint, session, redirect, url_for
from app.models import Link



get_url = Blueprint("get_url", __name__)

@get_url.route("/get_url/<type>", methods=["GET", "POST"])

def fetch_url(type="list"):
    '''
    Fetches user generated url.
    By default fetches top 10 latest user generated url with parameter set to 'list' by default.
    Otherwise, pass 'last' as arugument to fetch only the last generated url.
    '''
    if type.lower() != "list":
        fetch = 1
    else:
        fetch = 10


    if session.get("user_type") != "registered":
        url_list = Link.query.filter_by(anon_id=session.get("user_id")).limit(fetch).all()
    else:
        url_list = Link.query.filter_by(user_id=session.get("user_id")).limit(fetch).all()
    
    # lambda to map the items of url_list into the url_for() while other argument remain unchanged
    # The type parameter is an arguement for the main.index() fucntion
    url_list = list(map(lambda type:url_for("main.index", type, _external=True), url_list))


    return {url_list}