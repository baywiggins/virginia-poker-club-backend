from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import Config

# Initialize extensions
# db = SQLAlchemy()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions with the app instance
    # db.init_app(app)
    cors.init_app(app)

    # Register Blueprints
    from app.api.routes import bp as main_bp
    app.register_blueprint(main_bp)

    from app.calendar.routes import bp as calendar_bp
    app.register_blueprint(calendar_bp)

    return app
