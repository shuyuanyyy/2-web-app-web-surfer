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
def create_house():
    data = request.form
    current_user = get_jwt_identity()
    posted_admin = current_user

    #check if the user exists
    if not posted_admin:
        return jsonify({"error": "User not found"}), 404

    #check if the user is admin
    #if posted_admin.usertype != 1: 
    #    return jsonify({"error": "Permission denied: Only admins can add houses"}), 403

    full_address = f"{data.get('street_address', '').strip()} {data.get('city_address', '').strip()}".strip()
    #create corresponding policy data
    new_policy = Policy(
        pet_allowed=int(data.get("allows_pets", 0)),
        guarantor_accepted=int(data.get("guarantor_accepted", 0)),
        smoke_free=int(data.get("allows_smoking", 0))
    ).save()

    #create corresponding home feature data
    new_home_feature = HomeFeature(
        centralair=int(data.get("centralair", 0)),
        dishwasher=int(data.get("dishwasher", 0)),
        hardwoodfloor=int(data.get("hardwoodfloor", 0)),
        view=int(data.get("view", 0)),
        privateoutdoor=int(data.get("privateoutdoor", 0)),
        washerdryer=int(data.get("washerdryer", 0)),
        fridge=int(data.get("fridge", 0)),
        oven=int(data.get("oven", 0))
    ).save()

    #create corresponding amenity data
    new_amenities = BuildingAmenity(
        doorman=int(data.get("doorman", 0)),
        bikeroom=int(data.get("bikeroom", 0)),
        elevator=int(data.get("elevator", 0)),
        laundry=int(data.get("laundry", 0)),
        gym=int(data.get("gym", 0)),
        packageroom=int(data.get("packageroom", 0)),
        parking=int(data.get("parking", 0)),
        concierge=int(data.get("concierge", 0)),
        library=int(data.get("library", 0))
    ).save()

    building = Building.objects(name=data['buildingName']).first()
    if not building:
        building = Building(
            name=data.get("buildingName"),
            address=full_address,
            num_unit = 0,
            about_info="None"
        ).save()

    #create new house data
    new_house = House(
        building=data.get("buildingName"),  # Assume the building exists
        apt_num=data.get("apt_num"),
        price=float(data.get("price", 0)),  # Ensure float conversion
        bedroom=data.get("bedroom"),
        bathroom=data.get("bathroom"),
        area=data.get("area"),
        available_date=data.get("date").strftime("%Y-%m-%d"),
        address=full_address,
        posted_admin=posted_admin,
        about_info=data.get("about_info"),
        policy=new_policy,
        home_feature=new_home_feature,
        amenities=new_amenities,
        picture=data.get("picture", "")  # Handle missing picture safely
    ).save()

    #find the corresponding building information
   
    
    #add the unit number by 1
    building.update(inc__num_unit=1)


    return redirect(url_for("house.get_house", house_id = new_house.apt_num))


@house_bp.route('/create_page', methods=['GET'])
def create_house_page():
    return render_template("admin_create_apt.html")

@house_bp.route('/confirm-create', methods=['GET'])
def confirm_create():
    return render_template("post-apt.html")


#show all houses
@house_bp.route('/list', methods=['GET'])
def get_all_houses():
    
    search_term = request.args.get('q', '')
    
    # get all houses first
    houses = House.objects.only(
        "apt_num","building", "price", "bedroom", 
        "bathroom", "area", "available_date", "address", "picture"
    )
    
    # filter in Python
    house_list = []
    for house in houses:
        # If there's a search term, filter by building name or address
        if search_term and search_term.strip():
            # case-insensitive search
            search_term_lower = search_term.lower()
            
            # check if search term is in building name or address
            if (search_term_lower in house.building.lower() or 
                search_term_lower in house.address.lower()):
                
                house_dict = {
                    "apt_num": house.apt_num,
                    "building": house.building,
                    "price": house.price,
                    "bedroom": house.bedroom,
                    "bathroom": house.bathroom,
                    "area": house.area,
                    "available_date": house.available_date.strftime("%Y-%m-%d"),
                    "address": house.address,
                    "picture": house.picture
                }
                
                # extract city from address
                if ',' in house.address:
                    house_dict["city"] = house.address.split(',', 1)[1].strip()
                else:
                    house_dict["city"] = house.address
                    
                house_list.append(house_dict)
        else:
            # if no search term, include all houses
            house_dict = {
                "apt_num": house.apt_num,
                "building": house.building,
                "price": house.price,
                "bedroom": house.bedroom,
                "bathroom": house.bathroom,
                "area": house.area,
                "available_date": house.available_date.strftime("%Y-%m-%d") if house.available_date else None,
                "address": house.address,
                "picture": house.picture
            }
            
            # extract city from address
            if ',' in house.address:
                house_dict["city"] = house.address.split(',', 1)[1].strip()
            else:
                house_dict["city"] = house.address
                
            house_list.append(house_dict)
            
    return render_template("aptlist.html", houseInfo=house_list, search_term=search_term, target=search_term)

'''@house_bp.route('/list', methods=['GET'])
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
    return render_template("aptlist.html", houseInfo=house_list)'''


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
        "available_date": house.available_date.strftime('%Y-%m-%d') if house.available_date else None,
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

#edit house page
@house_bp.route('/edit/<house_id>', methods=['GET'])
def edit_house_page(house_id):
    house = House.objects(apt_num=house_id).first()

    if not house:
        return "House not found", 404

    return render_template("admin_apt_detail_edit.html", apt=house)



#update house information
@house_bp.route('/update/<house_id>', methods=['POST','PUT'])
def update_house(house_id):
    data = request.form
    house = House.objects(apt_num=house_id).first()


    if not house:
        return jsonify({"error": "House not found"}), 404

    house.update(
        set__building=data.get("buildingName", house.building),
        set__apt_num=data.get("apt_num", house.apt_num),
        set__price=float(data.get("price", house.price)),
        set__bedroom=data.get("bedroom", house.bedroom),
        set__bathroom=data.get("bathroom", house.bathroom),
        set__area=data.get("area", house.area),
        set__available_date=data.get("date", house.available_date.strftime("%Y-%m-%d")),
        set__address=data.get("street_address", house.address),
        set__posted_admin=house.posted_admin,  # Keep the original poster
        set__about_info=data.get("about_info", house.about_info),
        set__picture=data.get("picture", house.picture)
    )
    if house.policy:
        house.policy.update(
            set__pet_allowed=int(data.get("allows_pets", 0)),
            set__guarantor_accepted=int(data.get("guarantor_accepted", 0)),
            set__smoke_free=int(data.get("allows_smoking", 0))
        )

    # Update amenities (1 for yes, 0 for no)
    if house.amenities:
        house.amenities.update(
            set__doorman=int(data.get("doorman", 0)),
            set__bikeroom=int(data.get("bikeroom", 0)),
            set__elevator=int(data.get("elevator", 0)),
            set__laundry=int(data.get("laundry", 0)),
            set__gym=int(data.get("gym", 0)),
            set__packageroom=int(data.get("packageroom", 0)),
            set__parking=int(data.get("parking", 0)),
            set__concierge=int(data.get("concierge", 0)),
            set__library=int(data.get("library", 0))
        )

    # Update home features (1 for yes, 0 for no)
    if house.home_feature:
        house.home_feature.update(
            set__centralair=int(data.get("centralair", 0)),
            set__dishwasher=int(data.get("dishwasher", 0)),
            set__hardwoodfloor=int(data.get("hardwoodfloor", 0)),
            set__view=int(data.get("view", 0)),
            set__privateoutdoor=int(data.get("privateoutdoor", 0)),
            set__washerdryer=int(data.get("washerdryer", 0)),
            set__fridge=int(data.get("fridge", 0)),
            set__oven=int(data.get("oven", 0))
        )

    #updated_house = House.objects(apt_num=house_id).first()
    building = Building.objects(name=house.building).first()
    updated_house = House.objects(apt_num = house_id).first()
    return redirect(url_for("house.get_house", house_id = updated_house.apt_num))
    #return redirect(url_for("house.get_house", house_id=house.apt_num))
    #return jsonify({"message": "House updated successfully"}), 200
    #return redirect(url_for("house.get_house", house_id = house.apt_num))

@house_bp.route('/confirm-update/<house_id>', methods=['GET'])
def confirm_update(house_id):
    # house = House.objects(apt_num=house_id).first()
    house={
        "buildingName":request.args.get('buildingName', ''),
        "apt_num":request.args.get('apt_num', ''),
        "price":request.args.get('price', ''),
        "bedroom":request.args.get('bedroom', ''),
        "bathroom":request.args.get('bathroom', ''),
        "area":request.args.get('area', ''),
        "date":request.args.get('date', ''),
    }
    
    if not house:
        return jsonify({"error": "House not found"}), 404

    return render_template("update-apt.html", apt=house, q_message="Are you sure you want to update this apartment?")

@house_bp.route('/confirm-delete/<house_id>', methods=['GET'])
def confirm_delete(house_id):
    house = House.objects(apt_num=house_id).first()

    if not house:
        return jsonify({"error": "House not found"}), 404

    return render_template("delete-apt.html", apt=house, q_message="Are you sure you want to delete this apartment?")

# delete house
@house_bp.route('/delete/<house_id>', methods=['POST'])
def delete_house(house_id):
    if request.form.get("_method") == "DELETE":
        house = House.objects(apt_num=house_id).first()

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

    return redirect(url_for("house.get_all_houses"))
