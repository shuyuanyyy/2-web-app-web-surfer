from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
from models import House, Policy, HomeFeature, BuildingAmenity, UserInformation, Building
from bson import ObjectId

house_bp = Blueprint("house", __name__)

#create house
from flask import Blueprint, request, jsonify
from models import House

house_bp = Blueprint("house", __name__)

# CREATE HOUSE
@house_bp.route('/create', methods=['POST'])
@jwt_required()
def create_house():
    data = request.json
    current_user = get_jwt_identity()
    posted_admin = current_user

    #check if the user exists
    if not posted_admin:
        return jsonify({"error": "User not found"}), 404

    #check if the user is admin
    if posted_admin.usertype != 1: 
        return jsonify({"error": "Permission denied: Only admins can add houses"}), 403


    #create corresponding policy data
    new_policy = Policy(
        pet_allowed=data["policy"]["pet_allowed"],
        guarantor_accepted=data["policy"]["guarantor_accepted"],
        smoke_free=data["policy"]["smoke_free"]
    ).save()

    #create corresponding home feature data
    new_home_feature = HomeFeature(
        centralair=data["home_feature"]["centralair"],
        dishwasher=data["home_feature"]["dishwasher"],
        hardwoodfloor=data["home_feature"]["hardwoodfloor"],
        view=data["home_feature"]["view"],
        privateoutdoor=data["home_feature"]["privateoutdoor"],
        washerdryer=data["home_feature"]["washerdryer"],
        fridge=data["home_feature"]["fridge"],
        oven=data["home_feature"]["oven"]
    ).save()

    #create corresponding amenity data
    new_amenities = BuildingAmenity(
        doorman=data["amenities"]["doorman"],
        bikeroom=data["amenities"]["bikeroom"],
        elevator=data["amenities"]["elevator"],
        laundry=data["amenities"]["laundry"],
        gym=data["amenities"]["gym"],
        packageroom=data["amenities"]["packageroom"],
        parking=data["amenities"]["parking"],
        concierge=data["amenities"]["concierge"],
        library=data["amenities"]["library"]
    ).save()

    #create new house data
    new_house = House(
        building=data["building"], #assume the building exists
        apt_num=data["apt_num"],
        price=data["price"],
        bedroom=data["bedroom"],
        bathroom=data["bathroom"],
        area=data["area"],
        available_date=data["available_date"],
        address=data["address"],
        posted_admin=posted_admin["username"],
        about_info=data["about_info"],
        policy=new_policy,
        home_feature=new_home_feature,
        amenities=new_amenities,
        picture=data["picture"]
    ).save()

    #find the corresponding building information
    building = Building.objects(name=data['building']).first()
    if not building:
        return jsonify({'error': 'Building not found'}), 404
    
    #add the unit number by 1
    building.update(inc__num_unit=1)


    return jsonify({"message": "House added successfully"}), 201

#show all houses
@house_bp.route('/list', methods=['GET'])
def get_all_houses():
    #only show part of the data in houses
    houses = House.objects.only(
        "apt_num","building", "price", "bedroom", 
        "bathroom", "area", "available_date", "address", "picture"
    )

    house_list = []
    for house in houses:
        house_list.append({
            "apt_num": house.apt_num,
            "building" : house.building,
            "price": house.price,
            "bedroom": house.bedroom,
            "bathroom": house.bathroom,
            "area": house.area,
            "available_date": house.available_date.strftime("%Y-%m-%d"),
            "address": house.address,
            "picture": house.picture
        })
    return render_template("aptlist.html", houseInfo=house_list)


#get details of a specific house
@house_bp.route('/<house_id>', methods=['GET'])
def get_house(house_id):
    house = House.objects(apt_num=house_id).first()
    #house = House.objects(id=house_id).first()
    try:
        house = House.objects(apt_num=house_id).first()
    except:
        return jsonify({"error": "Invalid house ID format"}), 400
    if not house:
        return jsonify({"error": "House not found"}), 404
    
    #extract house information
    house_data = {
        "apt_num": house.apt_num,
        "price": house.price,
        "bedroom": house.bedroom,
        "bathroom": house.bathroom,
        "area": house.area,
        "available_date": house.available_date.strftime("%Y-%m-%d") if house.available_date else None,
        "address": house.address,
        "posted_admin": house.posted_admin,
        "about_info": house.about_info,
        "policy": {
            "pet_allowed": house.policy.pet_allowed,
            "guarantor_accepted": house.policy.guarantor_accepted,
            "smoke_free": house.policy.smoke_free
        } if house.policy else None,
        "home_feature": {
            "centralair": house.home_feature.centralair,
            "dishwasher": house.home_feature.dishwasher,
            "hardwoodfloor": house.home_feature.hardwoodfloor,
            "view": house.home_feature.view,
            "privateoutdoor": house.home_feature.privateoutdoor,
            "washerdryer": house.home_feature.washerdryer,
            "fridge": house.home_feature.fridge,
            "oven": house.home_feature.oven
        } if house.home_feature else None,
        "amenities": {
            "doorman": house.amenities.doorman,
            "bikeroom": house.amenities.bikeroom,
            "elevator": house.amenities.elevator,
            "laundry": house.amenities.laundry,
            "gym": house.amenities.gym,
            "packageroom": house.amenities.packageroom,
            "parking": house.amenities.parking,
            "concierge": house.amenities.concierge,
            "library": house.amenities.library
        } if house.amenities else None,
        "picture": house.picture
    }

    #extract corresponding building information
    building_info = None
    building = Building.objects(name = house.building).first()
    if building:
        building_info = {
            'name': building.name,
            'address': building.address,
            'num_unit': building.num_unit,
            'about_info': building.about_info
        }

    #return jsonify({
    #    "house": house_data,
    #    "building": building_info
    #}), 200
    return render_template("detail.html", apt = house, building=building)

#update house information
@house_bp.route('/update/<house_id>', methods=['PUT'])
def update_house(house_id):
    data = request.json
    house = House.objects(id=house_id).first()

    if not house:
        return jsonify({"error": "House not found"}), 404

    house.update(**data)
    return jsonify({"message": "House updated successfully"}), 200

# delete house
@house_bp.route('/delete/<house_id>', methods=['DELETE'])
def delete_house(house_id):
    house = House.objects(id=house_id).first()

    if not house:
        return jsonify({"error": "House not found"}), 404

    building = Building.objects(name=house.building).first()
    # delete corresponding policies, home features, and amenities data
    if house.policy:
        house.policy.delete()
    if house.home_feature:
        house.home_feature.delete()
    if house.amenities:
        house.amenities.delete()
    house.delete()

    if building and building.num_unit > 0:
        building.update(dec__num_unit=1)

    return jsonify({"message": "House deleted successfully"}), 200
