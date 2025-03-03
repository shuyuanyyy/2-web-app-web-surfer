# Web Application Exercise

A little exercise to build a web application following an agile development process. See the [instructions](instructions.md) for more detail.

## Product vision statement

See instructions. Delete this line and place the Product Vision Statement here.

## User stories
As an admin, I can moderate and remove fraudulent or misleading listings, so that the platform remains reliable for users.
User Stories

In software-students-spring2025/2-web-app-web-surfer;· shuyuanyyy opened 5 days ago
As a student, I can search all available rental buildings around my university, so that I can choose my preferred ones to reduce the commute time.
User Stories

In software-students-spring2025/2-web-app-web-surfer;· Rin-Qi opened last week
As a guest, I can search up a specific building for its availability, so that I have the availability of that building and can compare the price with other buildings
User Stories

In software-students-spring2025/2-web-app-web-surfer;· Rin-Qi opened last week
As a guest, I can view all prices of a specific apartment on the website, so that I know the price of the apartments available in the area.
User Stories

In software-students-spring2025/2-web-app-web-surfer;· Rin-Qi opened last week
As a tenant, I want to compare the prices of similar properties on the website, so that I can assess if I am overpaying and negotiate better with my landlord.
User Stories

In software-students-spring2025/2-web-app-web-surfer;· shuyuanyyy opened last week
As a landlord, I want to compare rental prices of similar properties in my area on the website, so that I can accurately price my rental.
User Stories

## Steps necessary to run the software
###Rental Surfer - Apartment Rental Management System
Rental Surfer is a comprehensive web application for managing apartment rentals. This system allows administrators to manage apartment listings and users, while guests can browse available apartments and save favorites to their wishlist.
###Features
User authentication with JWT
Role-based access control (Admin and Guest roles)
Apartment listing management
User management
Building information
Apartment details with amenities, home features and policies
Search functionality
###Setup Requirements
Prerequisites
Python 3.6 or higher
MongoDB installed and running
pip (Python package manager)
###Installation
Clone the repository:
   ```git clone https://github.com/your-repo/rental-surfer.git```
   ```cd rental-surfer```
Create and activate a virtual environment:
   ```python -m venv venv```
   ```source venv/bin/activate  # On Windows: venv\Scripts\activate```
Install the required packages:
   ```pip install flask flask-jwt-extended pymongo mongoengine python-dotenv```
Create a .env file in the project root with the following variables:
   ```MONGO_URI=mongodb://localhost:27017/SWE_Project2_Rental_Software```
   ```MONGO_DBNAME=SWE_Project2_Rental_Software```
   ```SECRET_KEY=SWE_Project2```
   ```JWT_SECRET_KEY=SWE_Project2```
   ```FLASK_PORT=6000```
   ```FLASK_ENV=development```
###Running the Application
Start MongoDB:
   ```mongod```
Navigate to the Back-End directory:
   ```cd Back-End```
Run the application:
   ```python test2.py```
Open your browser and go to:
   ```http://localhost:6000```
###Database Structure
The application uses the following MongoDB collections:
user_information: User accounts (admin and guests)
houses: Apartment listings
buildings: Building information
policies: Property policies
home_features: Features of individual apartments
building_amenities: Amenities provided by buildings
wishlists: Saved favorites for guests
###User Guide
###Authentication
Login:
Navigate to the login page (/login)
Enter your username and password
Click "Login"
Register:
From the login page, click "Register"
Fill out the registration form
To create an admin account, check the "Admin" checkbox
Click "Register"
###Admin User Workflow
After logging in as an admin, you'll be directed to the Admin Dashboard.
###Admin Dashboard
The Admin Dashboard provides two main options:
Manage Apartment: View and manage all apartment listings
Manage Guest: View and manage user accounts
###Apartment Management
View All Apartments:
From the Admin Dashboard, click "Manage Apartment"
You'll see a list of all apartments with basic information
###Search Apartments:
Use the search bar at the top of the apartment list page
Enter keywords related to the apartment (building name, location)
Click "Search"
###Create New Apartment:
From the navigation bar, click "Create"
Fill out the apartment form with the following details:
Basic information (building name, apartment number, price, etc.)
Policies (pets, smoking, guarantor)
Apartment amenities
Home features
Click "Create" to submit
Review the details on the confirmation page
Click "Yes" to confirm creation
###View Apartment Details:
Click on any apartment in the list to view its complete details
###Edit Apartment:
When viewing an apartment's details, click the "Edit" button
Update the information in the form
Click "Save" to submit changes
Review the changes on the confirmation page
Click "Yes" to confirm
###Delete Apartment:
From the apartment list, click the trash icon next to an apartment
Confirm the deletion on the confirmation page
Click "Yes" to permanently delete the apartment
###User Management
###View All Users:
From the Admin Dashboard, click "Manage Guest"
You'll see a list of all users
###Search Users:
Use the search bar at the top of the user list page
Enter a username
Click "Search"
Delete User:
Click the trash icon next to a user in the list
Confirm the deletion on the confirmation page
Click "Yes" to permanently delete the user
###Guest User Workflow
After logging in as a guest, you'll be directed to the apartment listing page.
Browse Apartments:
Scroll through the list of available apartments
Search Apartments:
Use the search bar at the top of the apartment list page
Enter keywords related to the apartment
Click "Search"
View Apartment Details:
Click on any apartment in the list to view its complete details
Details include basic information, policies, amenities, and home features
Add to Wishlist:
When viewing an apartment, click the heart icon to add it to your wishlist
View Profile and Wishlist:
Click on your username in the top-right corner
Your profile page displays your account information and wishlist
Sign Out:
From your profile page, click "Sign Out" to log out
###Data Management
MongoDB Data Structure
The application uses the following data models:
UserInformation:
Username, password, user type (admin/guest), email
House (Apartment):
Building, apartment number, price, bedroom count, bathroom count
Area, available date, address, about information
References to policy, home features, and amenities
Building:
Name, address, number of units, about information
Policy:
Pet allowed, guarantor accepted, smoke-free status
HomeFeature:
Central air, dishwasher, hardwood floor, view
Private outdoor space, washer/dryer, fridge, oven
BuildingAmenity:
Doorman, bike room, elevator, laundry, gym
Package room, parking, concierge, library
Wishlist:
References to user and house
###Data Flow
When an admin creates or updates an apartment, the data is stored in the houses collection along with references to associated policies, features, and amenities.
When a guest adds an apartment to their wishlist, a new entry is created in the wishlists collection with references to both the user and the apartment.
###Troubleshooting
Login Issues: Ensure that the MongoDB service is running and that your credentials are correct.
Missing Dependencies: Run pip install flask flask-jwt-extended pymongo mongoengine python-dotenv to install all required packages.
Database Connection: Verify that the MongoDB connection string in the .env file is correct.
Page Not Found: Ensure you're using the correct routes as defined in the application.
###Security Notes
The application uses JWT for authentication
Passwords should be properly hashed in a production environment
Environment variables should be properly secured
###Development and Extending
To extend the application:
Add new routes in the appropriate blueprint files
Create new templates in the templates directory
Update the data models in models.py as needed
Add new static assets in the static directory

## Task Boards

See instructions. Delete this line and place a link to the task boards here.
