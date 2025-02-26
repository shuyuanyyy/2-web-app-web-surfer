from flask import Flask
from flask_jwt_extended import JWTManager
from mongoengine import connect


from routes.login_routes import login_bp
from routes.house_routes import house_bp

app = Flask(__name__)
connect('SWE_Project2_Rental_Software', host='mongodb://localhost:27017/SWE_Project2_Rental_Software')
app.config["JWT_SECRET_KEY"] = "SWE_Project2"  
app.config["JWT_TOKEN_LOCATION"] = ["headers"]
jwt = JWTManager(app)

app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(house_bp, url_prefix="/house")



if __name__ == '__main__':
    app.run(debug=True)