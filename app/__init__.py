from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager

from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions with the app instance
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register Blueprints
    from app.api.routes import bp as main_bp
    app.register_blueprint(main_bp)

    from app.calendar.routes import bp as calendar_bp
    app.register_blueprint(calendar_bp)

    from app.api.login_functions import bp as login_bp
    app.register_blueprint(login_bp)

    return app
