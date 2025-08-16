Company Job Portal
Project Description
This is a web application built with the Django framework that functions as a company job portal. It allows administrators to post, update, and delete job openings, while a separate guest user flow enables job seekers to register, view job listings, and apply for positions.

Features
User Registration: Guests can create a new account with a unique username and password.

User Authentication: Separate login flows for guests and administrators.

Job Listing: All users (including guests) can view a list of available job openings.

Job Search: Users can search for job openings based on title, description, or location.

Job Details: Logged-in users can view the full details of a job opening.

Job Application: Logged-in users can apply for a job by submitting their personal details and a resume.

Admin Dashboard: A secure admin interface for managing job posts and viewing applications.

Prerequisites
Before you begin, ensure you have the following software installed on your machine:

Python 3.x: The project is built using Python.

Git: To clone the project repository.

Installation Guide
Follow these steps to get the project up and running on your local machine.

1. Clone the Repository
Open your terminal or command prompt and clone the project repository using the following command. Replace [your_repo_url] with the actual URL of your project's Git repository.

git clone [your_repo_url]


2. Navigate to the Project Directory
Change your current directory to the project's root folder.

cd Quiz3_Simbol


3. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.

python -m venv venv


4. Activate the Virtual Environment
Activate the virtual environment to isolate the project's packages.

On macOS/Linux:

source venv/bin/activate


On Windows:

.\venv\Scripts\activate


5. Install Dependencies
Install all the required Python packages listed in requirements.txt. If you don't have this file, you can create it by running pip freeze > requirements.txt after installing your packages.

pip install -r requirements.txt


Running the Project
1. Database Migrations
Apply the database migrations to set up the necessary tables for your project.

python manage.py makemigrations
python manage.py migrate


2. Create an Admin User
Create a superuser account to access the Django Admin dashboard and manage job listings.

python manage.py createsuperuser


Follow the on-screen prompts to set up a username, email, and password.

3. Run the Development Server
Start the Django development server to view the website.

python manage.py runserver


You can now access the application by navigating to http://127.0.0.1:8000/ in your web browser.

Usage
Guest User:

Register: Visit http://127.0.0.1:8000/accounts/register/ to create a new user account.

Login: Use the dedicated guest login page at http://127.0.0.1:8000/accounts/login/ to access the job listings.

Apply for a Job: After logging in, navigate to the job list, click on a job, and submit your application.

Admin User:

Login: Log in to the admin dashboard at http://127.0.0.1:8000/admin/ using the superuser account you created.

Manage Jobs: From the dashboard, you can add, edit, or delete job openings. You can also view all submitted job applications.
