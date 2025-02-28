import os
import sys
import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request, JWTManager
import pymongo
from functools import wraps
from mongoengine import connect
from bson.objectid import ObjectId
from dotenv import load_dotenv, dotenv_values

sys.path.append(os.path.abspath("Back-End/routes"))

from routes.login_routes import login_bp
from routes.house_routes import house_bp
from routes.user_management_routes import user_management_bp
from routes.building_routes import building_bp
from routes.message_routes import message_bp

load_dotenv()  # load environment variables from .env file


def create_app():
    """
    Create and configure the Flask application.
    returns: app: the Flask application object
    """

    app = Flask(__name__, 
                template_folder=os.path.abspath("../templates"),
                static_folder=os.path.abspath("static"))
    # load flask config from env variables
    app.secret_key = "SWE_Project2"
    config = dotenv_values()
    app.config.from_mapping(config)
    connect(os.getenv("MONGO_DBNAME"), host=os.getenv("MONGO_URI"))
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "SWE_Project2")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "SWE_Project2")
    app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
    app.config["SESSION_TYPE"] = "filesystem"
    jwt = JWTManager(app)
    PUBLIC_ROUTES = ["login.login", "login.register", "static", "home", "message.get_message"]

    @app.before_request
    def restricted_access():
        #print("All Available Endpoints:", [rule.endpoint for rule in app.url_map.iter_rules()])
        """ if request.endpoint:
            print("Request endpoint:", request.endpoint)
        if request.endpoint.startswith("static"):
            return  """
        if request.endpoint not in PUBLIC_ROUTES:
            try:
                verify_jwt_in_request()
                get_jwt_identity()
            except:
                return redirect(url_for("message.get_message",message="Please login first",redirect=url_for("login.login")))
                #return redirect(url_for("login.login"))

    app.register_blueprint(login_bp, url_prefix="/login")
    app.register_blueprint(house_bp, url_prefix="/house")
    app.register_blueprint(user_management_bp, url_prefix="/users")
    app.register_blueprint(building_bp, url_prefix="/building")
    app.register_blueprint(message_bp, url_prefix = "/message")


    @app.route("/")
    def home():
        return redirect(url_for("login.login"))
    return app


app = create_app()

if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "6000")
    FLASK_ENV = os.getenv("FLASK_ENV")
    print(f"FLASK_ENV: {FLASK_ENV}, FLASK_PORT: {FLASK_PORT}")
    app.run(port=FLASK_PORT, debug=True)



