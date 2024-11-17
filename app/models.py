from app import db
from sqlalchemy import func

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)

    links = db.relationship("Link", backref="owner", cascade="all, delete-orphan", lazy=True)

    def __repr__(self):
        return f"{self.username}"

    
class Link(db.Model):
    __tablename__ = "links"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), index=True) # Registered users id
    anon_id = db.Column(db.String(255), index=True) # Anonymous users id
    origin_link = db.Column(db.String(2048), nullable=False)
    short_link = db.Column(db.String(15), nullable=False, index=True, unique=True)
    created_at = db.Column(db.DateTime, nullable=True, default=func.now())
    clicks = db.Column(db.Integer, default=0)
    last_clicked = (db.DateTime)


    def __repr__(self):
        return f"{self.short_link}"