# Studybuddy-

## Prerequisites
- Python (3.x recommended)
- Django (installed via pip)
## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Alphatechbot/Studybuddy
Change to the projec directory:

Create a virtual environment (optional but recommended):
python -m venv venv

#Activate the virtual environment:
On Windows:
venv\Scripts\activate

#On macOS and Linux
source venv/bin/activate

#Install project dependencies:
pip install -r requirements.txt

#Run migrations to set up the database:
python manage.py migrate

#Create a superuser account (admin) for the Django admin panel
python manage.py createsuperuser


#Start the development server:
python manage.py runserver

#Your Django project should now be running locally at http://localhost:8000/.

#Open a web browser and visit the admin panel at http://localhost:8000/admin/. Log in with the superuser credentials you created earlier.
