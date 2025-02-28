from flask import Blueprint, jsonify, request
from flask import render_template, redirect, url_for, flash
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import UserInformation, Wishlist, House
from bson import ObjectId

user_management_bp = Blueprint("user_management", __name__)

@user_management_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def admin_dashboard():
    current_user = get_jwt_identity()
    admin_user = UserInformation.objects(username=current_user).first()
    return render_template("admin-dashboard.html", admin=admin_user)

# get all users list
@user_management_bp.route('/list', methods=['GET'])
@jwt_required()
def get_all_users():
    current_user = get_jwt_identity()
    admin_user = UserInformation.objects(username=current_user).first()

    if not admin_user:
        return jsonify({"error": "User not found"}), 404

    # check if user is admin
    if admin_user.usertype != 1:
        return jsonify({"error": "Permission denied: Only admins can view all users"}), 403

    # get all users information; or should we also contain password
    users = UserInformation.objects.exclude('password')

    user_list = []
    for user in users:
        user_list.append({
            "id": str(user.id),
            "username": user.username,
            "email": user.email,
            "usertype": user.usertype,
            "avatar": user.avatar
        })

    return render_template("userlist.html", users=user_list)


# detailed information of a single user
@user_management_bp.route('/<user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    try:
        user = UserInformation.objects(id=ObjectId(user_id)).exclude('password').first()
    except:
        return jsonify({"error": "Invalid user ID format"}), 400

    if not user:
        return jsonify({"error": "User not found"}), 404

    user_data = {
        "id": str(user.id),
        "username": user.username,
        "email": user.email,
        "usertype": user.usertype,
        "avatar": user.avatar
    }

    return jsonify(user_data), 200


# delete user
@user_management_bp.route('/delete/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    # verify current user identity
    current_user = get_jwt_identity()
    admin_user = UserInformation.objects(username=current_user).first()

    if not admin_user:
        return jsonify({"error": "User not found"}), 404

    if admin_user.usertype != 1:
        return jsonify({"error": "Permission denied: Only admins can delete users"}), 403

    # get the user to delete
    try:
        user = UserInformation.objects(id=ObjectId(user_id)).first()
    except:
        return jsonify({"error": "Invalid user ID format"}), 400

    if not user:
        return jsonify({"error": "User to delete not found"}), 404

    # admin should not delete their own account
    if str(user.id) == str(admin_user.id):
        return jsonify({"error": "You cannot delete your own admin account"}), 403

    # delete wishlist
    Wishlist.objects(user=user).delete()

    # delete user
    user.delete()

    return jsonify({"message": "User deleted successfully"}), 200



# get user's wishlist
@user_management_bp.route('/wishlist', methods=['GET'])
@jwt_required()
def get_wishlist():
    current_user = get_jwt_identity()
    user = UserInformation.objects(username=current_user).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    wishlist_items = Wishlist.objects(user=user)
    
    wishlist_data = []
    for item in wishlist_items:
        house = item.house
        wishlist_data.append({
            "wishlist_id": str(item.id),
            "house_id": str(house.id),
            "building": house.building,
            "price": house.price,
            "bedroom": house.bedroom,
            "bathroom": house.bathroom,
            "area": house.area,
            "available_date": house.available_date.strftime("%Y-%m-%d") if house.available_date else None,
            "address": house.address,
            "picture": house.picture
        })

    return jsonify(wishlist_data), 200


# Add house to wishlist, directly come with url
@user_management_bp.route('/wishlist/add/<house_id>', methods=['POST'])
@jwt_required()
def add_to_wishlist(house_id):
    current_user = get_jwt_identity()
    user = UserInformation.objects(username=current_user).first()

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    try:
        house = House.objects(id=ObjectId(house_id)).first()
    except:
        return jsonify({"error": "Invalid house ID format"}), 400
    
    if not house:
        return jsonify({"error": "House not found"}), 404
    
    # check if house is already in wishlist
    existing_wishlist = Wishlist.objects(user=user, house=house).first()
    if existing_wishlist:
        return jsonify({"error": "House already in wishlist"}), 400
    
    # add to wishlist
    new_wishlist = Wishlist(
        user=user,
        house=house
    ).save()
    
    return jsonify({"message": "House added to wishlist successfully"}), 201


# remove house from wishlist
@user_management_bp.route('/wishlist/remove/<wishlist_id>', methods=['DELETE'])
@jwt_required()
def remove_from_wishlist(wishlist_id):
    current_user = get_jwt_identity()
    user = UserInformation.objects(username=current_user).first()

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    try:
        wishlist_item = Wishlist.objects(id=ObjectId(wishlist_id)).first()
    except:
        return jsonify({"error": "Invalid wishlist ID format"}), 400
    
    if not wishlist_item:
        return jsonify({"error": "Wishlist item not found"}), 404
    
    # check if the wishlist belongs to the current user
    if str(wishlist_item.user.id) != str(user.id):
        return jsonify({"error": "Permission denied: This wishlist item doesn't belong to you"}), 403
    
    wishlist_item.delete()
    
    return jsonify({"message": "House removed from wishlist successfully"}), 200