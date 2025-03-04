# Web Application Exercise

A little exercise to build a web application following an agile development process. See the [instructions](instructions.md) for more detail.

## Product vision statement

Rental Surfer is a comprehensive apartment rental management web application that connects broker company and potential tenants by providing a user-friendly platform to list, search, and manage available rental properties efficiently. While administrators in the broker company can create, edit, delete housing postings and delete guests, clients, who logged in as guests, can only view and search the desired apartment.

## User stories

[User Stories](https://github.com/software-students-spring2025/2-web-app-web-surfer/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22User%20Stories%22)

- As an admin, I can moderate and remove fraudulent or misleading listings, so that the platform remains reliable for users.
- As a student, I can search all available rental buildings in my city, so that I can choose my preferred ones to reduce the commute time.
- As a guest, I can search up a specific building for its availability, so that I have the availability of that building and can compare the price with other buildings.
- As a guest, I can view all prices of a specific apartment on the website, so that I know the price of the apartments available in the area.
- As a tenant, I want to compare the prices of similar properties on the website, so that I can assess if I am overpaying and negotiate better with my landlord.
- As a landlord, I want to compare rental prices of similar properties in my area on the website, so that I can accurately price my rental.
- As a guest, I can save my favorite listings, so that I can compare them later and make a final decision more easily.
- As an administrator, I can post my housing details on the software, so that more people can see it and be interested in.
- As an administrator, I can manage the posted rentals, so that guests can have more accurate information about the current rental market.
- As an administrator, I can remove the unwanted guests, so that I can keep the information posted by the company private.
- As an administrator, I can search for a specific user, so that quickly remove they without going through the long list.

## Steps necessary to run the software

### Features

- User authentication with JWT
- Role-based access control (Admin and Guest roles)
- Apartment listing management
- User management
- Building information
- Apartment details with amenities, home features and policies
- Search functionality

### Setup Requirements

#### Prerequisites

- Python 3.6 or higher
- MongoDB installed and running
- pip (Python package manager)

#### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/rental-surfer.git
   cd rental-surfer
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install flask flask-jwt-extended pymongo mongoengine python-dotenv
   ```

4. Create a `.env` file in the **Back-End** directory with the following variables:
   ```
   MONGO_URI=mongodb://localhost:27017/SWE_Project2_Rental_Software
   MONGO_DBNAME=SWE_Project2_Rental_Software
   JWT_SECRET_KEY=SWE_Project2
   FLASK_PORT=6000
   FLASK_ENV=development
   ```

### Example Users

For testing purposes, the application includes default users:

- **Admin User**:

  - Username: Bob
  - Password: 1234567
  - Email: bob@example.com

- **Guest User**:
  - Username: Alex
  - Password: 1234567
  - Email: alex@example.com

You can use these credentials to test the application without registration.

### Running the Application

1. Start MongoDB:

   ```bash
   mongod
   ```

2. Navigate to the Back-End directory:

   ```bash
   cd Back-End
   ```

3. Initialize the database:

   ```bash
   python initial_data_load.py
   ```

4. Run the application:

   ```bash
   python test2.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:6000
   ```

### Website Guide

Depends on whether the user is logged in as an administrator, the functionality varies.
The capability of each type of user is listed below:

Rental Surfer
│── Guest
│ ├── View all available units
│ ├── View detail information of selected unit
│ ├── Search for units based on city or address  
│ ├── Add a unit to wishlist
│ ├── Go to profile page and view all units in the wishlist
│── Admin
│ ├── View all available units
│ ├── View detail information of selected unit
│ ├── Search for units based on city or address
│ ├── Go to profile page and view own profile info
│ ├── Post a new unit
│ ├── Edit a existing unit
│ ├── Delete a existing unit
│ ├── View all users
│ ├── Search for a specific user based on username or email address
│ ├── Delete existing users

**Detailed user guid below:**

#### Authentication

1. **Login**:

   - Navigate to the login page (`/login`)
   - Enter your username and password
   - Click "Login"

2. **Register**:
   - From the login page, click "Register"
   - Fill out the registration form
   - To create an admin account, check the "Admin" checkbox
   - Click "Register"

#### Admin User Workflow

After logging in as an admin, you'll be directed to the Admin Dashboard.

##### Admin Dashboard

The Admin Dashboard provides two main options:

- **Manage Apartment**: View and manage all apartment listings
- **Manage Guest**: View and manage user accounts

##### Apartment Management

1. **View All Apartments**:

   - From the Admin Dashboard, click "Manage Apartment"
   - You'll see a list of all apartments with basic information

2. **Search Apartments**:

   - Use the search bar at the top of the apartment list page
   - Enter keywords related to the apartment (building name, location)
   - Click "Search"
   - Note: the search bar only takes in accurate information. For example: searching LIC will not work for Long Island City

3. **Create New Apartment**:

   - From the navigation bar, click "Create"
   - Fill out the apartment form with the following details:
     - Basic information (building name, apartment number, price, etc.)
     - Policies
     - Apartment amenities
     - Home features
   - Click "Create" to submit
   - Review the details on the confirmation page
   - Click "Yes" to confirm creation

4. **View Apartment Details**:

   - Click on any apartment in the list to view its complete details

5. **Edit Apartment**:

   - When viewing an apartment's details, click the "Edit" button
   - Update the information in the form
   - Click "Save" to submit changes
   - Review the changes on the confirmation page
   - Click "Yes" to confirm

6. **Delete Apartment**:
   - From the apartment list, click the trash icon next to an apartment
   - Confirm the deletion on the confirmation page
   - Click "Yes" to permanently delete the apartment

##### User Management

1. **View All Users**:

   - From the Admin Dashboard, click "Manage Guest"
   - You'll see a list of all users

2. **Search Users**:

   - Use the search bar at the top of the user list page
   - Enter a username
   - Click "Search"

3. **Delete User**:
   - Click the trash icon next to a user in the list
   - Confirm the deletion on the confirmation page
   - Click "Yes" to permanently delete the user

#### Guest User Workflow

After logging in as a guest, you'll be directed to the apartment listing page.

1. **Browse Apartments**:

   - Scroll through the list of available apartments

2. **Search Apartments**:

   - Use the search bar at the top of the apartment list page
   - Enter keywords related to the apartment
   - Click "Search"

3. **View Apartment Details**:

   - Click on any apartment in the list to view its complete details
   - Details include basic information, policies, amenities, and home features

4. **Add to Wishlist**:

   - When viewing an apartment, click the heart icon to add it to your wishlist

5. **View Profile and Wishlist**:

   - Click on your username in the top-right corner
   - Your profile page displays your account information and wishlist

6. **Sign Out**:
   - From your profile page, click "Sign Out" to log out

#### Data Flow

- When an admin creates or updates an apartment, the data is stored in the houses collection along with references to associated policies, features, and amenities.
- When a guest adds an apartment to their wishlist, a new entry is created in the wishlists collection with references to both the user and the apartment.

### Troubleshooting

- **Login Issues**: Ensure that the MongoDB service is running and that your credentials are correct.
- **Missing Dependencies**: Run `pip install flask flask-jwt-extended pymongo mongoengine python-dotenv` to install all required packages.
- **Database Connection**: Verify that the MongoDB connection string in the `.env` file is correct.
- **Page Not Found**: Ensure you're using the correct routes as defined in the application.
- **CSS Not Loaded**: Change line 30 (`static_folder=os.path.abspath("../static")`)in test2.py file in the Back-end directory to `static_folder=os.path.abspath("static"))`

### Security Notes

- The application uses JWT for authentication
- Passwords should be properly hashed in a production environment
- Environment variables should be properly secured

## Task Boards

- [Link to our project task board sprint 1](https://github.com/orgs/software-students-spring2025/projects/14)
- [Link to our project task board sprint 2](https://github.com/orgs/software-students-spring2025/projects/121)
