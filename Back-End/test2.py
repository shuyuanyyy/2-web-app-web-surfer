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
from routes.message_routes import message_bp

load_dotenv()  # load environment variables from .env file


def create_app():
    """
    Create and configure the Flask application.
    returns: app: the Flask application object
    """

    app = Flask(__name__, 
                template_folder=os.path.abspath("../templates"),
                static_folder=os.path.abspath("../static"))
    # load flask config from env variables
    app.secret_key = "SWE_Project2"
    config = dotenv_values()
    app.config.from_mapping(config)
    connect(os.getenv("MONGO_DBNAME"), host=os.getenv("MONGO_URI"))
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "SWE_Project2")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "SWE_Project2")
    app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["SESSION_PERMANENT"] = True

    app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]  # Ensure JWT is read from both
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "SWE_Project2")
    app.config["JWT_ACCESS_COOKIE_NAME"] = "access_token_cookie"
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False  # Disable CSRF for debugging
    app.config["JWT_COOKIE_SECURE"] = False


    jwt = JWTManager(app)
    PUBLIC_ROUTES = ["login.login", "login.register", "static", "home", "message.get_message"]

    @app.before_request
    def restricted_access():
        #print(f"DEBUG: Checking request to {request.endpoint}")

        if request.endpoint not in PUBLIC_ROUTES:
            try:
                # Print all request headers before authentication check
                #print("DEBUG: Incoming Request Headers:", dict(request.headers))
                #print("DEBUG: Incoming Request Cookies:", dict(request.cookies))

                # If Authorization is missing, manually inject JWT from cookies
                if "Authorization" not in request.headers:
                    jwt_from_cookie = request.cookies.get("access_token_cookie")
                    if jwt_from_cookie:
                        request.headers = {**request.headers, "Authorization": f"Bearer {jwt_from_cookie}"}
                        #print("DEBUG: Injected JWT from Cookie into Headers")

                verify_jwt_in_request()
                identity = get_jwt_identity()
                #print(f"DEBUG: User {identity} is authenticated.")
            except Exception as e:
                #print(f"DEBUG: JWT verification failed - {str(e)}")
                return redirect(url_for("message.get_message", message="Please login first", redirect=url_for("login.login")))


    
    app.register_blueprint(login_bp, url_prefix="/login")
    app.register_blueprint(house_bp, url_prefix="/house")
    app.register_blueprint(user_management_bp, url_prefix="/users")
    app.register_blueprint(message_bp, url_prefix = "/message")


    @app.route("/")
    def home():
        return redirect(url_for("login.login"))
    

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html')
    
    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template('404.html')
    
    @app.errorhandler(500)
    def error(e):
        return render_template('message.html',message="error",redirectWebsite=url_for(home))
    
    return app


app = create_app()

if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "6000")
    FLASK_ENV = os.getenv("FLASK_ENV")
    print(f"FLASK_ENV: {FLASK_ENV}, FLASK_PORT: {FLASK_PORT}")
    app.run(port=FLASK_PORT, debug=True)



