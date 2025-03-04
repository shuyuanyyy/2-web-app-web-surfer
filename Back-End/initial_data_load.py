#Note: This file served as a file to load pre-coded data into mongo db. Should be only run once.
#      Run this file will delete all of the existing document and collections

from mongoengine import Document, StringField, IntField, EmailField, ReferenceField, DateField, FloatField
from datetime import datetime
from mongoengine import connect
from pymongo import MongoClient

connect('SWE_Project2_Rental_Software', host='mongodb://localhost:27017/SWE_Project2_Rental_Software')

#Drop collection if exist to prevent uniqueness error
client = MongoClient()
db = client["SWE_Project2_Rental_Software"]
existing_collections = db.list_collection_names()
for collection in existing_collections:
    db[collection].drop()
    print(f"Collection '{collection}' dropped.")


#user-information table
class UserInformation(Document):
    meta = {'collection': 'user_information'}
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    usertype = IntField(required=True)  # 1 for admin, 0 for guest
    avatar = StringField()
    email = EmailField(required=True, unique=True)

#policies table
class Policy(Document):
    meta = {'collection': 'policies'}
    # 1 for yes, 0 for no
    pet_allowed = IntField(required=True)  
    guarantor_accepted = IntField(required=True)  
    smoke_free = IntField(required=True)  

#home features table
class HomeFeature(Document):
    meta = {'collection': 'home_features'}
    # 1 for yes, 0 for no
    centralair = IntField(required=True)
    dishwasher = IntField(required=True)
    hardwoodfloor = IntField(required=True)
    view = IntField(required=True)
    privateoutdoor = IntField(required=True)
    washerdryer = IntField(required=True)
    fridge = IntField(required=True)
    oven = IntField(required=True)

#building amenities table
class BuildingAmenity(Document):
    meta = {'collection': 'building_amenities'}
    # 1 for yes, 0 for no
    doorman = IntField(required=True)
    bikeroom = IntField(required=True)
    elevator = IntField(required=True)
    laundry = IntField(required=True)
    gym = IntField(required=True)
    packageroom = IntField(required=True)
    parking = IntField(required=True)
    concierge = IntField(required=True)
    library = IntField(required=True)

#buildings table
class Building(Document):
    meta = {'collection': 'buildings'}
    name = StringField(required=True)
    address = StringField(required=True)
    num_unit = IntField(required=True)
    about_info = StringField(required=True)

#houses table
class House(Document):
    meta = {'collection': 'houses'}
    building = StringField(required=True)
    apt_num = StringField(required=True)
    price = FloatField(required=True)
    bedroom = StringField(required=True)
    bathroom = StringField(required=True)
    area = StringField(required=True)
    available_date = DateField(required=True)
    address = StringField(required=True)
    posted_admin = StringField(required=True)
    about_info = StringField()
    policy = ReferenceField(Policy, required=True)
    home_feature = ReferenceField(HomeFeature, required=True)
    amenities = ReferenceField(BuildingAmenity, required=True)
    picture = StringField()


#wishlists table
class Wishlist(Document):
    meta = {'collection': 'wishlists'}
    user = ReferenceField(UserInformation, required=True)
    house = ReferenceField(House, required=True)


#Insert data


 #Insert a user
user_guest_1 = UserInformation(
    username="Alex",
    password="1234567",
    usertype=0,
    avatar="...",
    email="alex@example.com"
).save()
user_admin_2 = UserInformation(
    username="Bob",
    password="1234567",
    usertype=1,
    avatar="...",
    email="bob@example.com"
).save()
user_admin_3 = UserInformation(
    username="Charlie",
    password="1234567",
    usertype=1,
    avatar="...",
    email="charlie@example.com"
).save()
user_admin_4 = UserInformation(
    username="David",
    password="1234567",
    usertype=1,
    avatar="...",
    email="david@example.com"
).save()
user_guest_5 = UserInformation(
    username="Emma",
    password="1234567",
    usertype=0,
    avatar="...",
    email="emma@example.com"
).save()
user_guest_6 = UserInformation(
    username="Fiona",
    password="1234567",
    usertype=0,
    avatar="...",
    email="fiona@example.com"
).save()
user_guest_7 = UserInformation(
    username="George",
    password="1234567",
    usertype=0,
    avatar="...",
    email="george@example.com"
).save()
user_guest_8 = UserInformation(
    username="Hannah",
    password="1234567",
    usertype=0,
    avatar="...",
    email="hannah@example.com"
).save()
user_guest_9 = UserInformation(
    username="Ian",
    password="1234567",
    usertype=0,
    avatar="...",
    email="ian@example.com"
).save()
user_guest_10 = UserInformation(
    username="Julia",
    password="1234567",
    usertype=0,
    avatar="...",
    email="julia@example.com"
).save()
user_guest_11 = UserInformation(
    username="Kevin",
    password="1234567",
    usertype=0,
    avatar="...",
    email="kevin@example.com"
).save()
user_guest_12 = UserInformation(
    username="Laura",
    password="1234567",
    usertype=0,
    avatar="...",
    email="laura@example.com"
).save()
user_guest_13 = UserInformation(
    username="Michael",
    password="1234567",
    usertype=0,
    avatar="...",
    email="michael@example.com"
).save()
user_guest_14 = UserInformation(
    username="Nina",
    password="1234567",
    usertype=0,
    avatar="...",
    email="nina@example.com"
).save()
user_guest_15 = UserInformation(
    username="Oscar",
    password="1234567",
    usertype=0,
    avatar="...",
    email="oscar@example.com"
).save()
user_guest_16 = UserInformation(
    username="Paula",
    password="1234567",
    usertype=0,
    avatar="...",
    email="paula@example.com"
).save()
user_guest_17 = UserInformation(
    username="Quincy",
    password="1234567",
    usertype=0,
    avatar="...",
    email="quincy@example.com"
).save()
user_guest_18 = UserInformation(
    username="Rachel",
    password="1234567",
    usertype=0,
    avatar="...",
    email="rachel@example.com"
).save()
user_guest_19 = UserInformation(
    username="Steve",
    password="1234567",
    usertype=0,
    avatar="...",
    email="steve@example.com"
).save()
user_guest_20 = UserInformation(
    username="Tina",
    password="1234567",
    usertype=0,
    avatar="...",
    email="tina@example.com"
).save()
user_guest_21 = UserInformation(
    username="Uma",
    password="1234567",
    usertype=0,
    avatar="...",
    email="uma@example.com"
).save()
user_guest_22 = UserInformation(
    username="Victor",
    password="1234567",
    usertype=0,
    avatar="...",
    email="victor@example.com"
).save()
user_guest_23 = UserInformation(
    username="Wendy",
    password="1234567",
    usertype=0,
    avatar="...",
    email="wendy@example.com"
).save()
user_guest_24 = UserInformation(
    username="Xavier",
    password="1234567",
    usertype=0,
    avatar="...",
    email="xavier@example.com"
).save()
user_guest_25 = UserInformation(
    username="Yvonne",
    password="1234567",
    usertype=0,
    avatar="...",
    email="yvonne@example.com"
).save()
user_guest_26 = UserInformation(
    username="Zack",
    password="1234567",
    usertype=0,
    avatar="...",
    email="zack@example.com"
).save()
user_guest_27 = UserInformation(
    username="Alice",
    password="1234567",
    usertype=0,
    avatar="...",
    email="alice@example.com"
).save()
user_guest_28 = UserInformation(
    username="Brian",
    password="1234567",
    usertype=0,
    avatar="...",
    email="brian@example.com"
).save()
user_guest_29 = UserInformation(
    username="Catherine",
    password="1234567",
    usertype=0,
    avatar="...",
    email="catherine@example.com"
).save()
user_guest_30 = UserInformation(
    username="Daniel",
    password="1234567",
    usertype=0,
    avatar="...",
    email="daniel@example.com"
).save()



 #Insert House

policy_0 = Policy(
    pet_allowed=0,
    guarantor_accepted=0,
    smoke_free=1
).save()

home_feature_0 = HomeFeature(
    centralair=1,
    dishwasher=0,
    hardwoodfloor=0,
    view=1,
    privateoutdoor=1,
    washerdryer=0,
    fridge=1,
    oven=0
).save()

amenities_0 = BuildingAmenity(
    doorman=0,
    bikeroom=1,
    elevator=1,
    laundry=0,
    gym=0,
    packageroom=1,
    parking=0,
    concierge=1,
    library=1
).save()

house_0 = House(
    building="Jackson Park",
    apt_num="#100",
    price=2818.73,
    bedroom="1",
    bathroom="2.5",
    area="854",
    available_date=datetime(2025, 1, 10),
    address="28-16 Jackson Ave, Long Island City, NY 11101",
    posted_admin="Emma",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_0,
    home_feature=home_feature_0,
    amenities=amenities_0,
    picture="..."
).save()

policy_1 = Policy(
    pet_allowed=1,
    guarantor_accepted=1,
    smoke_free=0
).save()

home_feature_1 = HomeFeature(
    centralair=0,
    dishwasher=0,
    hardwoodfloor=1,
    view=0,
    privateoutdoor=0,
    washerdryer=1,
    fridge=0,
    oven=1
).save()

amenities_1 = BuildingAmenity(
    doorman=0,
    bikeroom=0,
    elevator=1,
    laundry=0,
    gym=1,
    packageroom=1,
    parking=0,
    concierge=1,
    library=1
).save()

house_1 = House(
    building="Central Plaza",
    apt_num="#101",
    price=1410.23,
    bedroom="Studio",
    bathroom="1.5",
    area="816",
    available_date=datetime(2025, 2, 15),
    address="10 Main St, New York, NY 10001",
    posted_admin="Catherine",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_1,
    home_feature=home_feature_1,
    amenities=amenities_1,
    picture="..."
).save()

policy_2 = Policy(
    pet_allowed=0,
    guarantor_accepted=0,
    smoke_free=1
).save()

home_feature_2 = HomeFeature(
    centralair=0,
    dishwasher=0,
    hardwoodfloor=1,
    view=1,
    privateoutdoor=1,
    washerdryer=1,
    fridge=1,
    oven=0
).save()

amenities_2 = BuildingAmenity(
    doorman=1,
    bikeroom=0,
    elevator=0,
    laundry=0,
    gym=1,
    packageroom=1,
    parking=1,
    concierge=1,
    library=0
).save()

house_2 = House(
    building="Ocean View",
    apt_num="#102",
    price=1692.26,
    bedroom="3",
    bathroom="2.5",
    area="1738",
    available_date=datetime(2025, 2, 8),
    address="10 Main St, New York, NY 10001",
    posted_admin="David",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_2,
    home_feature=home_feature_2,
    amenities=amenities_2,
    picture="..."
).save()

policy_3 = Policy(
    pet_allowed=0,
    guarantor_accepted=1,
    smoke_free=0
).save()

home_feature_3 = HomeFeature(
    centralair=0,
    dishwasher=1,
    hardwoodfloor=0,
    view=0,
    privateoutdoor=1,
    washerdryer=1,
    fridge=0,
    oven=0
).save()

amenities_3 = BuildingAmenity(
    doorman=0,
    bikeroom=1,
    elevator=0,
    laundry=0,
    gym=0,
    packageroom=1,
    parking=0,
    concierge=0,
    library=0
).save()

house_3 = House(
    building="Greenwood Residences",
    apt_num="#103",
    price=4812.57,
    bedroom="3",
    bathroom="3",
    area="1943",
    available_date=datetime(2025, 6, 15),
    address="10 Main St, New York, NY 10001",
    posted_admin="Alice",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_3,
    home_feature=home_feature_3,
    amenities=amenities_3,
    picture="..."
).save()

policy_4 = Policy(
    pet_allowed=0,
    guarantor_accepted=1,
    smoke_free=0
).save()

home_feature_4 = HomeFeature(
    centralair=1,
    dishwasher=1,
    hardwoodfloor=0,
    view=1,
    privateoutdoor=0,
    washerdryer=1,
    fridge=0,
    oven=0
).save()

amenities_4 = BuildingAmenity(
    doorman=1,
    bikeroom=1,
    elevator=0,
    laundry=0,
    gym=0,
    packageroom=1,
    parking=1,
    concierge=1,
    library=0
).save()

house_4 = House(
    building="Skyline Towers",
    apt_num="#104",
    price=1951.11,
    bedroom="2",
    bathroom="1.5",
    area="652",
    available_date=datetime(2025, 12, 17),
    address="10 Main St, New York, NY 10001",
    posted_admin="Yvonne",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_4,
    home_feature=home_feature_4,
    amenities=amenities_4,
    picture="..."
).save()

policy_5 = Policy(
    pet_allowed=0,
    guarantor_accepted=1,
    smoke_free=1
).save()

home_feature_5 = HomeFeature(
    centralair=1,
    dishwasher=1,
    hardwoodfloor=0,
    view=0,
    privateoutdoor=1,
    washerdryer=1,
    fridge=0,
    oven=1
).save()

amenities_5 = BuildingAmenity(
    doorman=0,
    bikeroom=0,
    elevator=1,
    laundry=0,
    gym=1,
    packageroom=1,
    parking=0,
    concierge=1,
    library=1
).save()

house_5 = House(
    building="Sunset Apartments",
    apt_num="#105",
    price=2698.68,
    bedroom="Studio",
    bathroom="2",
    area="447",
    available_date=datetime(2025, 3, 5),
    address="12 Sunset Dr, Los Angeles, CA 90027",
    posted_admin="Bob",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_5,
    home_feature=home_feature_5,
    amenities=amenities_5,
    picture="..."
).save()

policy_6 = Policy(
    pet_allowed=1,
    guarantor_accepted=1,
    smoke_free=0
).save()

home_feature_6 = HomeFeature(
    centralair=1,
    dishwasher=0,
    hardwoodfloor=0,
    view=1,
    privateoutdoor=0,
    washerdryer=1,
    fridge=0,
    oven=0
).save()

amenities_6 = BuildingAmenity(
    doorman=1,
    bikeroom=0,
    elevator=0,
    laundry=1,
    gym=0,
    packageroom=0,
    parking=0,
    concierge=1,
    library=1
).save()

house_6 = House(
    building="Lakeside Manor",
    apt_num="#106",
    price=1932.13,
    bedroom="Studio",
    bathroom="1",
    area="595",
    available_date=datetime(2025, 2, 26),
    address="12 Sunset Dr, Los Angeles, CA 90027",
    posted_admin="Julia",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_6,
    home_feature=home_feature_6,
    amenities=amenities_6,
    picture="..."
).save()

policy_7 = Policy(
    pet_allowed=0,
    guarantor_accepted=1,
    smoke_free=1
).save()

home_feature_7 = HomeFeature(
    centralair=0,
    dishwasher=0,
    hardwoodfloor=0,
    view=0,
    privateoutdoor=1,
    washerdryer=1,
    fridge=1,
    oven=0
).save()

amenities_7 = BuildingAmenity(
    doorman=0,
    bikeroom=0,
    elevator=1,
    laundry=1,
    gym=0,
    packageroom=1,
    parking=1,
    concierge=0,
    library=0
).save()

house_7 = House(
    building="Cityscape Condos",
    apt_num="#107",
    price=2709.35,
    bedroom="2",
    bathroom="2",
    area="1392",
    available_date=datetime(2025, 4, 2),
    address="12 Sunset Dr, Los Angeles, CA 90027",
    posted_admin="David",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_7,
    home_feature=home_feature_7,
    amenities=amenities_7,
    picture="..."
).save()

policy_8 = Policy(
    pet_allowed=1,
    guarantor_accepted=0,
    smoke_free=0
).save()

home_feature_8 = HomeFeature(
    centralair=1,
    dishwasher=0,
    hardwoodfloor=1,
    view=1,
    privateoutdoor=1,
    washerdryer=0,
    fridge=1,
    oven=1
).save()

amenities_8 = BuildingAmenity(
    doorman=1,
    bikeroom=1,
    elevator=1,
    laundry=0,
    gym=0,
    packageroom=0,
    parking=0,
    concierge=1,
    library=0
).save()

house_8 = House(
    building="The Grand Heights",
    apt_num="#108",
    price=2470.22,
    bedroom="1",
    bathroom="3",
    area="1184",
    available_date=datetime(2025, 3, 5),
    address="12 Sunset Dr, Los Angeles, CA 90027",
    posted_admin="Alice",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_8,
    home_feature=home_feature_8,
    amenities=amenities_8,
    picture="..."
).save()

policy_9 = Policy(
    pet_allowed=1,
    guarantor_accepted=1,
    smoke_free=1
).save()

home_feature_9 = HomeFeature(
    centralair=0,
    dishwasher=1,
    hardwoodfloor=1,
    view=1,
    privateoutdoor=0,
    washerdryer=1,
    fridge=0,
    oven=0
).save()

amenities_9 = BuildingAmenity(
    doorman=0,
    bikeroom=1,
    elevator=0,
    laundry=1,
    gym=0,
    packageroom=0,
    parking=1,
    concierge=0,
    library=0
).save()

house_9 = House(
    building="Maplewood Suites",
    apt_num="#109",
    price=4742.86,
    bedroom="1",
    bathroom="1.5",
    area="511",
    available_date=datetime(2025, 11, 5),
    address="305 Maple St, Portland, OR 97209",
    posted_admin="Ian",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_9,
    home_feature=home_feature_9,
    amenities=amenities_9,
    picture="..."
).save()

policy_10 = Policy(
    pet_allowed=0,
    guarantor_accepted=0,
    smoke_free=0
).save()

home_feature_10 = HomeFeature(
    centralair=1,
    dishwasher=1,
    hardwoodfloor=0,
    view=1,
    privateoutdoor=0,
    washerdryer=1,
    fridge=0,
    oven=1
).save()

amenities_10 = BuildingAmenity(
    doorman=0,
    bikeroom=0,
    elevator=0,
    laundry=0,
    gym=1,
    packageroom=1,
    parking=1,
    concierge=1,
    library=0
).save()

house_10 = House(
    building="Harbor Point",
    apt_num="#110",
    price=3443.9,
    bedroom="3",
    bathroom="2.5",
    area="1489",
    available_date=datetime(2025, 2, 3),
    address="88 Dockside Dr, Boston, MA 02110",
    posted_admin="Rachel",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_10,
    home_feature=home_feature_10,
    amenities=amenities_10,
    picture="..."
).save()

policy_11 = Policy(
    pet_allowed=1,
    guarantor_accepted=1,
    smoke_free=1
).save()

home_feature_11 = HomeFeature(
    centralair=1,
    dishwasher=0,
    hardwoodfloor=0,
    view=0,
    privateoutdoor=1,
    washerdryer=0,
    fridge=0,
    oven=1
).save()

amenities_11 = BuildingAmenity(
    doorman=0,
    bikeroom=0,
    elevator=0,
    laundry=0,
    gym=0,
    packageroom=0,
    parking=0,
    concierge=1,
    library=0
).save()

house_11 = House(
    building="Riverbend Lofts",
    apt_num="#111",
    price=888.13,
    bedroom="Studio",
    bathroom="2",
    area="1177",
    available_date=datetime(2025, 8, 2),
    address="60 Riverside Rd, Minneapolis, MN 55401",
    posted_admin="Victor",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_11,
    home_feature=home_feature_11,
    amenities=amenities_11,
    picture="..."
).save()

policy_12 = Policy(
    pet_allowed=1,
    guarantor_accepted=0,
    smoke_free=0
).save()

home_feature_12 = HomeFeature(
    centralair=1,
    dishwasher=1,
    hardwoodfloor=1,
    view=0,
    privateoutdoor=1,
    washerdryer=0,
    fridge=1,
    oven=1
).save()

amenities_12 = BuildingAmenity(
    doorman=1,
    bikeroom=1,
    elevator=1,
    laundry=1,
    gym=1,
    packageroom=0,
    parking=0,
    concierge=1,
    library=1
).save()

house_12 = House(
    building="Pinecrest Homes",
    apt_num="#112",
    price=1143.92,
    bedroom="2",
    bathroom="3",
    area="978",
    available_date=datetime(2025, 12, 22),
    address="40 Pine Rd, Atlanta, GA 30303",
    posted_admin="Catherine",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_12,
    home_feature=home_feature_12,
    amenities=amenities_12,
    picture="..."
).save()

policy_13 = Policy(
    pet_allowed=0,
    guarantor_accepted=0,
    smoke_free=0
).save()

home_feature_13 = HomeFeature(
    centralair=0,
    dishwasher=0,
    hardwoodfloor=1,
    view=1,
    privateoutdoor=1,
    washerdryer=1,
    fridge=0,
    oven=1
).save()

amenities_13 = BuildingAmenity(
    doorman=1,
    bikeroom=0,
    elevator=1,
    laundry=1,
    gym=0,
    packageroom=0,
    parking=0,
    concierge=1,
    library=0
).save()

house_13 = House(
    building="The Pearl",
    apt_num="#113",
    price=1244.77,
    bedroom="2",
    bathroom="2",
    area="939",
    available_date=datetime(2025, 4, 3),
    address="55 Oceanview Blvd, San Diego, CA 92101",
    posted_admin="Oscar",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_13,
    home_feature=home_feature_13,
    amenities=amenities_13,
    picture="..."
).save()

policy_14 = Policy(
    pet_allowed=1,
    guarantor_accepted=1,
    smoke_free=0
).save()

home_feature_14 = HomeFeature(
    centralair=1,
    dishwasher=0,
    hardwoodfloor=1,
    view=0,
    privateoutdoor=0,
    washerdryer=0,
    fridge=1,
    oven=0
).save()

amenities_14 = BuildingAmenity(
    doorman=0,
    bikeroom=0,
    elevator=1,
    laundry=1,
    gym=1,
    packageroom=0,
    parking=0,
    concierge=1,
    library=0
).save()

house_14 = House(
    building="Westwood Residences",
    apt_num="#114",
    price=1855.06,
    bedroom="1",
    bathroom="2",
    area="588",
    available_date=datetime(2025, 6, 13),
    address="35 Westwood Ave, Dallas, TX 75201",
    posted_admin="Laura",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_14,
    home_feature=home_feature_14,
    amenities=amenities_14,
    picture="..."
).save()

policy_15 = Policy(
    pet_allowed=0,
    guarantor_accepted=1,
    smoke_free=0
).save()

home_feature_15 = HomeFeature(
    centralair=0,
    dishwasher=1,
    hardwoodfloor=1,
    view=1,
    privateoutdoor=0,
    washerdryer=1,
    fridge=0,
    oven=0
).save()

amenities_15 = BuildingAmenity(
    doorman=0,
    bikeroom=1,
    elevator=1,
    laundry=1,
    gym=0,
    packageroom=0,
    parking=0,
    concierge=1,
    library=1
).save()

house_15 = House(
    building="Sky Harbor",
    apt_num="#115",
    price=1190.99,
    bedroom="1",
    bathroom="2",
    area="1336",
    available_date=datetime(2025, 3, 17),
    address="99 Flightpath Rd, Phoenix, AZ 85034",
    posted_admin="Emma",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_15,
    home_feature=home_feature_15,
    amenities=amenities_15,
    picture="..."
).save()

policy_16 = Policy(
    pet_allowed=1,
    guarantor_accepted=1,
    smoke_free=1
).save()

home_feature_16 = HomeFeature(
    centralair=1,
    dishwasher=1,
    hardwoodfloor=0,
    view=0,
    privateoutdoor=1,
    washerdryer=0,
    fridge=0,
    oven=0
).save()

amenities_16 = BuildingAmenity(
    doorman=0,
    bikeroom=1,
    elevator=1,
    laundry=0,
    gym=0,
    packageroom=0,
    parking=0,
    concierge=1,
    library=0
).save()

house_16 = House(
    building="Bayside Towers",
    apt_num="#116",
    price=4146.73,
    bedroom="1",
    bathroom="1",
    area="1877",
    available_date=datetime(2025, 8, 4),
    address="21 Seaside Dr, Tampa, FL 33602",
    posted_admin="Brian",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_16,
    home_feature=home_feature_16,
    amenities=amenities_16,
    picture="..."
).save()

policy_17 = Policy(
    pet_allowed=0,
    guarantor_accepted=1,
    smoke_free=0
).save()

home_feature_17 = HomeFeature(
    centralair=0,
    dishwasher=1,
    hardwoodfloor=1,
    view=1,
    privateoutdoor=0,
    washerdryer=1,
    fridge=1,
    oven=1
).save()

amenities_17 = BuildingAmenity(
    doorman=1,
    bikeroom=0,
    elevator=1,
    laundry=0,
    gym=0,
    packageroom=0,
    parking=0,
    concierge=1,
    library=0
).save()

house_17 = House(
    building="The Summit",
    apt_num="#117",
    price=4864.97,
    bedroom="2",
    bathroom="1.5",
    area="1880",
    available_date=datetime(2025, 4, 10),
    address="15 Mountain View Ln, Salt Lake City, UT 84101",
    posted_admin="Tina",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_17,
    home_feature=home_feature_17,
    amenities=amenities_17,
    picture="..."
).save()

policy_18 = Policy(
    pet_allowed=1,
    guarantor_accepted=0,
    smoke_free=0
).save()

home_feature_18 = HomeFeature(
    centralair=1,
    dishwasher=1,
    hardwoodfloor=1,
    view=1,
    privateoutdoor=0,
    washerdryer=0,
    fridge=1,
    oven=0
).save()

amenities_18 = BuildingAmenity(
    doorman=0,
    bikeroom=0,
    elevator=1,
    laundry=1,
    gym=0,
    packageroom=0,
    parking=0,
    concierge=0,
    library=0
).save()

house_18 = House(
    building="Parkside Lofts",
    apt_num="#118",
    price=3539.04,
    bedroom="1",
    bathroom="1",
    area="849",
    available_date=datetime(2025, 1, 20),
    address="9 Central Park Ave, New York, NY 10019",
    posted_admin="Julia",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_18,
    home_feature=home_feature_18,
    amenities=amenities_18,
    picture="..."
).save()

policy_19 = Policy(
    pet_allowed=0,
    guarantor_accepted=0,
    smoke_free=1
).save()

home_feature_19 = HomeFeature(
    centralair=0,
    dishwasher=0,
    hardwoodfloor=0,
    view=0,
    privateoutdoor=1,
    washerdryer=1,
    fridge=1,
    oven=0
).save()

amenities_19 = BuildingAmenity(
    doorman=0,
    bikeroom=0,
    elevator=1,
    laundry=0,
    gym=0,
    packageroom=0,
    parking=1,
    concierge=1,
    library=1
).save()

house_19 = House(
    building="Metropolitan Suites",
    apt_num="#119",
    price=4950.2,
    bedroom="2",
    bathroom="2",
    area="825",
    available_date=datetime(2025, 7, 16),
    address="88 Metro Blvd, Miami, FL 33130",
    posted_admin="Nina",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_19,
    home_feature=home_feature_19,
    amenities=amenities_19,
    picture="..."
).save()

policy_20 = Policy(
    pet_allowed=0,
    guarantor_accepted=0,
    smoke_free=1
).save()

home_feature_20 = HomeFeature(
    centralair=0,
    dishwasher=0,
    hardwoodfloor=0,
    view=0,
    privateoutdoor=1,
    washerdryer=0,
    fridge=1,
    oven=0
).save()

amenities_20 = BuildingAmenity(
    doorman=1,
    bikeroom=1,
    elevator=0,
    laundry=1,
    gym=0,
    packageroom=0,
    parking=1,
    concierge=1,
    library=0
).save()

house_20 = House(
    building="Horizon Towers",
    apt_num="#120",
    price=929.69,
    bedroom="1",
    bathroom="3",
    area="743",
    available_date=datetime(2025, 6, 24),
    address="77 Skyline Rd, San Jose, CA 95110",
    posted_admin="Michael",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_20,
    home_feature=home_feature_20,
    amenities=amenities_20,
    picture="..."
).save()

policy_21 = Policy(
    pet_allowed=0,
    guarantor_accepted=1,
    smoke_free=1
).save()

home_feature_21 = HomeFeature(
    centralair=1,
    dishwasher=0,
    hardwoodfloor=1,
    view=1,
    privateoutdoor=0,
    washerdryer=0,
    fridge=1,
    oven=1
).save()

amenities_21 = BuildingAmenity(
    doorman=1,
    bikeroom=0,
    elevator=0,
    laundry=0,
    gym=1,
    packageroom=1,
    parking=1,
    concierge=0,
    library=0
).save()

house_21 = House(
    building="The Ivory",
    apt_num="#121",
    price=2712.84,
    bedroom="3",
    bathroom="2.5",
    area="1041",
    available_date=datetime(2025, 4, 8),
    address="34 Whitehouse Ave, Washington, DC 20001",
    posted_admin="Wendy",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_21,
    home_feature=home_feature_21,
    amenities=amenities_21,
    picture="..."
).save()

policy_22 = Policy(
    pet_allowed=0,
    guarantor_accepted=1,
    smoke_free=0
).save()

home_feature_22 = HomeFeature(
    centralair=1,
    dishwasher=1,
    hardwoodfloor=0,
    view=1,
    privateoutdoor=1,
    washerdryer=1,
    fridge=0,
    oven=1
).save()

amenities_22 = BuildingAmenity(
    doorman=0,
    bikeroom=1,
    elevator=0,
    laundry=0,
    gym=1,
    packageroom=1,
    parking=1,
    concierge=1,
    library=0
).save()

house_22 = House(
    building="Uptown Heights",
    apt_num="#122",
    price=1037.47,
    bedroom="3",
    bathroom="1.5",
    area="1539",
    available_date=datetime(2025, 4, 28),
    address="50 Uptown St, Charlotte, NC 28202",
    posted_admin="Paula",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_22,
    home_feature=home_feature_22,
    amenities=amenities_22,
    picture="..."
).save()

policy_23 = Policy(
    pet_allowed=0,
    guarantor_accepted=1,
    smoke_free=0
).save()

home_feature_23 = HomeFeature(
    centralair=1,
    dishwasher=0,
    hardwoodfloor=1,
    view=1,
    privateoutdoor=1,
    washerdryer=0,
    fridge=0,
    oven=0
).save()

amenities_23 = BuildingAmenity(
    doorman=0,
    bikeroom=1,
    elevator=1,
    laundry=1,
    gym=0,
    packageroom=1,
    parking=0,
    concierge=0,
    library=1
).save()

house_23 = House(
    building="Lush Gardens",
    apt_num="#123",
    price=2051.81,
    bedroom="Studio",
    bathroom="1.5",
    area="1927",
    available_date=datetime(2025, 4, 21),
    address="22 Green Ave, Houston, TX 77002",
    posted_admin="Fiona",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_23,
    home_feature=home_feature_23,
    amenities=amenities_23,
    picture="..."
).save()

policy_24 = Policy(
    pet_allowed=0,
    guarantor_accepted=1,
    smoke_free=0
).save()

home_feature_24 = HomeFeature(
    centralair=1,
    dishwasher=0,
    hardwoodfloor=0,
    view=1,
    privateoutdoor=0,
    washerdryer=0,
    fridge=1,
    oven=0
).save()

amenities_24 = BuildingAmenity(
    doorman=1,
    bikeroom=0,
    elevator=1,
    laundry=0,
    gym=0,
    packageroom=1,
    parking=1,
    concierge=1,
    library=0
).save()

house_24 = House(
    building="The Haven",
    apt_num="#124",
    price=3386.5,
    bedroom="Studio",
    bathroom="1",
    area="1515",
    available_date=datetime(2025, 1, 15),
    address="10 Serenity Ln, Nashville, TN 37201",
    posted_admin="Catherine",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_24,
    home_feature=home_feature_24,
    amenities=amenities_24,
    picture="..."
).save()

policy_25 = Policy(
    pet_allowed=1,
    guarantor_accepted=1,
    smoke_free=0
).save()

home_feature_25 = HomeFeature(
    centralair=1,
    dishwasher=1,
    hardwoodfloor=1,
    view=1,
    privateoutdoor=0,
    washerdryer=1,
    fridge=0,
    oven=0
).save()

amenities_25 = BuildingAmenity(
    doorman=1,
    bikeroom=0,
    elevator=1,
    laundry=0,
    gym=0,
    packageroom=0,
    parking=0,
    concierge=1,
    library=1
).save()

house_25 = House(
    building="Seaview Apartments",
    apt_num="#125",
    price=1505.25,
    bedroom="Studio",
    bathroom="1.5",
    area="1754",
    available_date=datetime(2025, 9, 12),
    address="300 Beach Blvd, Honolulu, HI 96815",
    posted_admin="Alex",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_25,
    home_feature=home_feature_25,
    amenities=amenities_25,
    picture="..."
).save()

policy_26 = Policy(
    pet_allowed=1,
    guarantor_accepted=1,
    smoke_free=0
).save()

home_feature_26 = HomeFeature(
    centralair=1,
    dishwasher=1,
    hardwoodfloor=0,
    view=0,
    privateoutdoor=1,
    washerdryer=0,
    fridge=1,
    oven=0
).save()

amenities_26 = BuildingAmenity(
    doorman=1,
    bikeroom=1,
    elevator=0,
    laundry=0,
    gym=1,
    packageroom=1,
    parking=1,
    concierge=1,
    library=0
).save()

house_26 = House(
    building="Royal Manor",
    apt_num="#126",
    price=3296.26,
    bedroom="1",
    bathroom="2.5",
    area="1206",
    available_date=datetime(2025, 3, 16),
    address="123 Crown Rd, Las Vegas, NV 89109",
    posted_admin="Julia",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_26,
    home_feature=home_feature_26,
    amenities=amenities_26,
    picture="..."
).save()

policy_27 = Policy(
    pet_allowed=1,
    guarantor_accepted=0,
    smoke_free=0
).save()

home_feature_27 = HomeFeature(
    centralair=1,
    dishwasher=1,
    hardwoodfloor=1,
    view=1,
    privateoutdoor=1,
    washerdryer=0,
    fridge=1,
    oven=0
).save()

amenities_27 = BuildingAmenity(
    doorman=1,
    bikeroom=1,
    elevator=1,
    laundry=0,
    gym=1,
    packageroom=0,
    parking=0,
    concierge=0,
    library=0
).save()

house_27 = House(
    building="Emerald Towers",
    apt_num="#127",
    price=2485.67,
    bedroom="2",
    bathroom="1.5",
    area="565",
    available_date=datetime(2025, 8, 6),
    address="18 Crystal Ave, Orlando, FL 32801",
    posted_admin="Nina",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_27,
    home_feature=home_feature_27,
    amenities=amenities_27,
    picture="..."
).save()

policy_28 = Policy(
    pet_allowed=0,
    guarantor_accepted=1,
    smoke_free=1
).save()

home_feature_28 = HomeFeature(
    centralair=0,
    dishwasher=0,
    hardwoodfloor=1,
    view=0,
    privateoutdoor=0,
    washerdryer=0,
    fridge=1,
    oven=1
).save()

amenities_28 = BuildingAmenity(
    doorman=0,
    bikeroom=0,
    elevator=1,
    laundry=0,
    gym=0,
    packageroom=0,
    parking=0,
    concierge=1,
    library=1
).save()

house_28 = House(
    building="The Veranda",
    apt_num="#128",
    price=2851.44,
    bedroom="1",
    bathroom="1",
    area="579",
    available_date=datetime(2025, 7, 24),
    address="28 Palm Rd, Charleston, SC 29401",
    posted_admin="Uma",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_28,
    home_feature=home_feature_28,
    amenities=amenities_28,
    picture="..."
).save()

policy_29 = Policy(
    pet_allowed=0,
    guarantor_accepted=1,
    smoke_free=0
).save()

home_feature_29 = HomeFeature(
    centralair=0,
    dishwasher=1,
    hardwoodfloor=1,
    view=1,
    privateoutdoor=0,
    washerdryer=0,
    fridge=0,
    oven=0
).save()

amenities_29 = BuildingAmenity(
    doorman=0,
    bikeroom=0,
    elevator=0,
    laundry=1,
    gym=1,
    packageroom=1,
    parking=1,
    concierge=1,
    library=0
).save()

house_29 = House(
    building="Summit Residences",
    apt_num="#129",
    price=4724.45,
    bedroom="3",
    bathroom="1",
    area="539",
    available_date=datetime(2025, 6, 15),
    address="45 Peak St, Denver, CO 80203",
    posted_admin="Bob",
    about_info="Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    policy=policy_29,
    home_feature=home_feature_29,
    amenities=amenities_29,
    picture="..."
).save()


# Insert into wishlist
wishlist_1 = Wishlist(
    user=user_guest_1,
    house=house_1
).save()

wishlist_2 = Wishlist(
    user=user_guest_1,
    house=house_2
).save()

wishlist_3 = Wishlist(
    user=user_guest_1,
    house=house_3
).save()


print("Data inserted successfully!")
