from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Building, UserInformation, House
from bson import ObjectId

message_bp = Blueprint("message", __name__)

# get all buildings list
@message_bp.route('/message', methods=['GET'])
def get_message():
    message = request.args.get("message", "No message provided")  
    redirectWebsite = request.args.get("redirect", "/")  

    return render_template("message.html", message=message, redirectWebsite=redirectWebsite)
