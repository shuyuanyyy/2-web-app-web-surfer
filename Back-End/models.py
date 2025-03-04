from mongoengine import Document, StringField, IntField, EmailField, ReferenceField, DateField, FloatField
from datetime import datetime
from mongoengine import connect

connect('SWE_Project2_Rental_Software', host='mongodb://localhost:27017/SWE_Project2_Rental_Software')

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
    apt_num = StringField(required=True, unique=True)
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

