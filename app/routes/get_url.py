from flask import Blueprint, session, url_for
from app.models import Link
from flask import jsonify



get_url = Blueprint("get_url", __name__)

@get_url.route("/get_url/<string:type>", methods=["GET"])

def fetch_url(type:str='list'):
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
    
    # Using list comprehension to generate a list of urls for user short links
    url_list = [
        url_for("main.redirect_to_link", url=link.short_link, _external=True) for link in url_list
    ]


    return jsonify({"urls": url_list})