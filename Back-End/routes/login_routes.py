from models import UserInformation
from flask_jwt_extended import create_access_token, set_access_cookies
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session

#login_bp = Blueprint("login", __name__)
login_bp = Blueprint("login", __name__, 
                     template_folder="../../templates")

#User Registration
@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    print('Inside register route')
    if request.method == 'GET':
        print('Render register.html')
        return render_template("register.html")

    data = request.form
    existing_user = UserInformation.objects(username=data["username"]).first()
    if existing_user:
        #return jsonify({"error": "Username already exists"}), 400
        return redirect(url_for("message.get_message",message="Username already exists",redirect=url_for("login.register")))
        #return render_template("register.html", error="Username already exists")
    
    new_user = UserInformation(
        username = data['username'],
        password = data['password'],
        usertype=data.get("usertype",0), #change
        avatar = data.get('avatar',""),
        email=data['email']
    ).save()

    #return jsonify({
    #    "message": "User registered successfully"
    #    }), 201 
    return redirect(url_for("message.get_message",message="Username register successfully",redirect=url_for("login.login")))
    #return redirect(url_for('login.login')) 

#User Login
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    data = request.form
    isAdmin = 1 if data.get("isAdmin") == "on" else 0
    user = UserInformation.objects(username=data["username"], password=data["password"], usertype=isAdmin).first()
    if not user:
        #return jsonify({"error": "Invalid username or password"}), 401
        #return render_template("login.html", error="Invalid username or password")
        return redirect(url_for("message.get_message",message="Invalid username or password",redirect=url_for("login.login")))
    
    access_token = create_access_token(identity=user.username)
    session['access_token'] = access_token
    response = redirect(url_for("user_management.admin_dashboard" if isAdmin == 1 else "house.get_all_houses"))
    
    set_access_cookies(response, access_token)
    return response


    #return jsonify({"message": "Login successful",
    #    'usertype': user.usertype,
    #    'access_token': access_token}
    #    ), 200
    