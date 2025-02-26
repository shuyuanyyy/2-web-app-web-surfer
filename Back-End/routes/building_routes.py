from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Building, UserInformation, House
from bson import ObjectId

building_bp = Blueprint("building", __name__)

# get all buildings list
@building_bp.route('/list', methods=['GET'])
def get_buildings():
    buildings = Building.objects()
    
    building_list = []
    for building in buildings:
        building_list.append({
            "id": str(building.id),
            "name": building.name,
            "address": building.address,
            "num_unit": building.num_unit,
            "about_info": building.about_info
        })
    
    return jsonify(building_list), 200

# get building details
@building_bp.route('/<building_id>', methods=['GET'])
def get_building(building_id):
    try:
        building = Building.objects(id=ObjectId(building_id)).first()
    except:
        return jsonify({"error": "Invalid building ID format"}), 400
    
    if not building:
        return jsonify({"error": "Building not found"}), 404
    
    # get houses in the building
    houses = House.objects(building=building.name).only(
        "apt_num", "price", "bedroom", "bathroom", "area", 
        "available_date", "address", "picture"
    )
    
    house_list = []
    for house in houses:
        house_list.append({
            "id": str(house.id),
            "apt_num": house.apt_num,
            "price": house.price,
            "bedroom": house.bedroom,
            "bathroom": house.bathroom,
            "area": house.area,
            "available_date": house.available_date.strftime("%Y-%m-%d") if house.available_date else None,
            "picture": house.picture
        })
    
    building_data = {
        "id": str(building.id),
        "name": building.name,
        "address": building.address,
        "num_unit": building.num_unit,
        "about_info": building.about_info,
        "units": house_list
    }
    
    return jsonify(building_data), 200

# create new building
@building_bp.route('/create', methods=['POST'])
@jwt_required()
def create_building():
    # check if user is admin
    current_user = get_jwt_identity()
    admin_user = UserInformation.objects(username=current_user).first()
    
    if not admin_user:
        return jsonify({"error": "User not found"}), 404
    
    if admin_user.usertype != 1:
        return jsonify({"error": "Permission denied: Only admins can add buildings"}), 403
    
    data = request.json
    
    # check if name already exists
    existing_building = Building.objects(name=data.get('name')).first()
    if existing_building:
        return jsonify({"error": "Building with this name already exists"}), 400
    
    # create new building
    try:
        new_building = Building(
            name=data.get('name'),
            address=data.get('address'),
            num_unit=data.get('num_unit', 0),  # Default to 0 if not provided
            about_info=data.get('about_info', '')  # Default to empty string if not provided
        ).save()
        
        building_data = {
            "id": str(new_building.id),
            "name": new_building.name,
            "address": new_building.address,
            "num_unit": new_building.num_unit,
            "about_info": new_building.about_info
        }
        
        return jsonify({
            "message": "Building created successfully",
            "building": building_data
        }), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# update building information
@building_bp.route('/update/<building_id>', methods=['PUT'])
@jwt_required()
def update_building(building_id):
    # check if user is admin
    current_user = get_jwt_identity()
    admin_user = UserInformation.objects(username=current_user).first()
    
    if not admin_user:
        return jsonify({"error": "User not found"}), 404
    
    if admin_user.usertype != 1:
        return jsonify({"error": "Permission denied: Only admins can update buildings"}), 403
    
    try:
        building = Building.objects(id=ObjectId(building_id)).first()
    except:
        return jsonify({"error": "Invalid building ID format"}), 400
    
    if not building:
        return jsonify({"error": "Building not found"}), 404
    
    data = request.json
    
    # if name is being changed, check if new name already exists
    if 'name' in data and data['name'] != building.name:
        existing_building = Building.objects(name=data['name']).first()
        if existing_building:
            return jsonify({"error": "Building with this name already exists"}), 400
        
        # if name is changing, we need to update all houses with this building name
        if data['name'] != building.name:
            House.objects(building=building.name).update(building=data['name'])
    
    try:
        building.update(**data)
        
        updated_building = Building.objects(id=ObjectId(building_id)).first()
        building_data = {
            "id": str(updated_building.id),
            "name": updated_building.name,
            "address": updated_building.address,
            "num_unit": updated_building.num_unit,
            "about_info": updated_building.about_info
        }
        
        return jsonify({
            "message": "Building updated successfully",
            "building": building_data
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# delete building
@building_bp.route('/delete/<building_id>', methods=['DELETE'])
@jwt_required()
def delete_building(building_id):
    # check if user is admin
    current_user = get_jwt_identity()
    admin_user = UserInformation.objects(username=current_user).first()
    
    if not admin_user:
        return jsonify({"error": "User not found"}), 404
    
    if admin_user.usertype != 1:
        return jsonify({"error": "Permission denied: Only admins can delete buildings"}), 403
    
    try:
        building = Building.objects(id=ObjectId(building_id)).first()
    except:
        return jsonify({"error": "Invalid building ID format"}), 400
    
    if not building:
        return jsonify({"error": "Building not found"}), 404
    
    # check if there are houses associated with this building ***not sure if to have this
    houses = House.objects(building=building.name)
    if houses:
        return jsonify({
            "error": "Cannot delete building with existing houses. Please delete all houses in this building first.",
            "house_count": len(houses)
        }), 400
    
    # delete building
    building.delete()
    
    return jsonify({"message": "Building deleted successfully"}), 200