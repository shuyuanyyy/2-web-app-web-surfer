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
    if not admin_user or admin_user.usertype != 1:
        return redirect(url_for("message.get_message", message="Access denied. Admin required.", redirect=url_for("login.login")))
    
    return render_template("admin-dashboard.html", admin=admin_user)

# get all users list
@user_management_bp.route('/list', methods=['GET'])
@jwt_required()
def get_all_users():
    current_user = get_jwt_identity()
    admin_user = UserInformation.objects(username=current_user).first()

    # get search query parameter
    search_term = request.args.get('q', '')
    
    if not admin_user:
        return jsonify({"error": "User not found"}), 404
    # check if user is admin
    if admin_user.usertype != 1:
        return jsonify({"error": "Permission denied: Only admins can view all users"}), 403

    # filter users based on search term if it exists
    if search_term and search_term.strip():
        # create a regex pattern for case-insensitive search
        regex_pattern = f'.*{search_term}.*'
        # search for users where username or email matches the pattern
        username_matches = UserInformation.objects(username__iregex=regex_pattern).exclude('password')
        email_matches = UserInformation.objects(email__iregex=regex_pattern).exclude('password')
        
        # Ccmbine the query results
        user_ids = set()
        users = []
        
        for user in username_matches:
            if str(user.id) not in user_ids:
                users.append(user)
                user_ids.add(str(user.id))
                
        for user in email_matches:
            if str(user.id) not in user_ids:
                users.append(user)
                user_ids.add(str(user.id))
    else:
        # get all users information if no search term
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

    return render_template("userlist.html", usersInfo=user_list, search_term=search_term, target=search_term)


# detailed information of a single user
@user_management_bp.route('/profile/<user_name>', methods=['GET'])
@jwt_required()
def get_user(user_name):
    current_user = get_jwt_identity()
    logged_in_user = UserInformation.objects(username=current_user).first()
    
    # special case for the hardcoded profile link in base.html
    if user_name == '67b8d6f05da61bc65fceb190':
        # redirect
        return redirect(url_for('user_management.get_user', user_name=current_user))
    
    try:
        user = UserInformation.objects(username=user_name).exclude('password').first()
    except:
        return redirect(url_for("message.get_message", message="Invalid user format", redirect=url_for("house.get_all_houses")))

    if not user:
        return redirect(url_for("message.get_message", message="User not found", redirect=url_for("house.get_all_houses")))
    
    # if the current user is admin or looking at their own profile
    if logged_in_user.usertype != 1 and current_user != user_name:
        return redirect(url_for("message.get_message", message="Permission denied: You can only view your own profile", redirect=url_for("house.get_all_houses")))
    
    user_data = {
        "id": str(user.id),
        "username": user.username,
        "email": user.email,
        "usertype": user.usertype,
        "avatar": user.avatar
    }
    
    # get user's wishlist items if guest
    wishlist_data = []
    if user.usertype == 0:
        wishlist_items = Wishlist.objects(user=user)
        
        for item in wishlist_items:
            house = item.house
            wishlist_data.append({
                "building": house.building,
                "apt_num": house.apt_num,
                "price": house.price,
                "bedroom": house.bedroom,
                "bathroom": house.bathroom,
                "area": house.area,
                "available_date": house.available_date.strftime("%Y-%m-%d") if house.available_date else None,
                "city": house.address.split(',', 1)[1].strip() if ',' in house.address else house.address,
                "picture": house.picture
            })

    return render_template("profile.html", userInfo=user_data, houseInfo=wishlist_data)


# delete user
@user_management_bp.route('/delete/<user_name>', methods=['POST'])
@jwt_required()
def delete_user(user_name):
    # verify current user identity
    current_user = get_jwt_identity()
    admin_user = UserInformation.objects(username=current_user).first()

    if not admin_user:
        return redirect(url_for("message.get_message", message="User not found", redirect=url_for("login.login")))
    
    if admin_user.usertype != 1:
        return redirect(url_for("message.get_message", message="Permission denied: Only admins can delete users", redirect=url_for("house.get_all_houses")))

    # get the user to delete
    try:
        user = UserInformation.objects(username=user_name).first()
    except:
        return redirect(url_for("message.get_message", message="Invalid user format", redirect=url_for("user_management.get_all_users")))
    if not user:
        return redirect(url_for("message.get_message", message="User to delete not found", redirect=url_for("user_management.get_all_users")))

    # admin should not delete their own account
    if user.username == admin_user.username:
        return redirect(url_for("message.get_message", message="You cannot delete your own admin account", redirect=url_for("user_management.get_all_users")))

    # Instead of deleting, show confirmation page
    return render_template("delete-user.html", 
                      q_message="Are you sure that you want to delete this user?",
                      username=user_name,
                      email=user.email)
    
@user_management_bp.route('/confirm-delete/<user_name>', methods=['POST'])
@jwt_required()
def confirm_delete_user(user_name):
    # verify current user identity
    current_user = get_jwt_identity()
    admin_user = UserInformation.objects(username=current_user).first()

    if not admin_user:
        return redirect(url_for("message.get_message", message="User not found", redirect=url_for("login.login")))
    
    if admin_user.usertype != 1:
        return redirect(url_for("message.get_message", message="Permission denied: Only admins can delete users", redirect=url_for("house.get_all_houses")))

    # get the user to delete
    try:
        user = UserInformation.objects(username=user_name).first()
    except:
        return redirect(url_for("message.get_message", message="Invalid user format", redirect=url_for("user_management.get_all_users")))
    if not user:
        return redirect(url_for("message.get_message", message="User to delete not found", redirect=url_for("user_management.get_all_users")))

    # admin should not delete their own account
    if user.username == admin_user.username:
        return redirect(url_for("message.get_message", message="You cannot delete your own admin account", redirect=url_for("user_management.get_all_users")))

    Wishlist.objects(user=user).delete()

    # delete user
    user.delete()

    return redirect(url_for("message.get_message", message="User deleted successfully", redirect=url_for("user_management.get_all_users")))



# add house to wishlist, directly come with url
@user_management_bp.route('/wishlist/add/<house_id>', methods=['POST'])
@jwt_required()
def add_to_wishlist(house_id):
    current_user = get_jwt_identity()
    user = UserInformation.objects(username=current_user).first()

    if not user:
        return redirect(url_for("message.get_message", message="User not found", redirect=url_for("login.login")))
    
    house = House.objects(apt_num=house_id).first()
    
    if not house:
        return redirect(url_for("message.get_message", message="House not found", redirect=url_for("house.get_all_houses")))
    
    # check if house is already in wishlist
    existing_wishlist = Wishlist.objects(user=user, house=house).first()
    if existing_wishlist:
        return redirect(url_for("message.get_message", message="House already in wishlist", redirect=url_for("house.get_house", house_id=house.apt_num)))
    
    # add to wishlist
    new_wishlist = Wishlist(
        user=user,
        house=house
    ).save()
    
    return redirect(url_for("message.get_message", message="House added to wishlist successfully", redirect=url_for("house.get_house", house_id=house.apt_num)))


# remove house from wishlist
'''@user_management_bp.route('/wishlist/remove/<wishlist_id>', methods=['DELETE'])
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
    
    return jsonify({"message": "House removed from wishlist successfully"}), 200'''