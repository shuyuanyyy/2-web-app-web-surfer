from models import UserInformation
from flask_jwt_extended import create_access_token
from flask import Blueprint, request, jsonify

login_bp = Blueprint("login", __name__)

#User Registration
@login_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    existing_user = UserInformation.objects(username=data["username"]).first()
    if existing_user:
        return jsonify({"error": "Username already exists"}), 400
    
    new_user = UserInformation(
        username = data['username'],
        password = data['password'],
        usertype=data.get("usertype",0), #change
        avatar = data.get('avatar',""),
        email=data['email']
    ).save()

    return jsonify({
        "message": "User registered successfully"
        }), 201    

#User Login
@login_bp.route('/login',methods=["POST"])
def login():
    data = request.json
    user = UserInformation.objects(username=data["username"], password=data["password"]).first()
    if not user:
        return jsonify({"error": "Invalid username or password"}), 401
    
    access_token = create_access_token(identity=user.username)

    return jsonify({"message": "Login successful",
        'usertype': user.usertype,
        'access_token': access_token}
        ), 200
