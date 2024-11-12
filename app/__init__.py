from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import main, signup, login, logout
    app.register_blueprint(main.main)
    app.register_blueprint(signup.signup, url_prefix="/auth")
    app.register_blueprint(login.login, url_prefix="/auth")
    app.register_blueprint(logout.logout)

    return app