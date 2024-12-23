from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///chained.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = "securecookie"
    SESSION_COOKIE_NAME = "chained_session_id"
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)
    