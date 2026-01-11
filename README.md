# Create venv
python -m venv env

# Create Django Project     
django-admin startproject todo_main . 

# Create Super User
 ### Step 1- Migrate
            python manage.py migrate
 ### Step 2 - Create Superuser
            python manage.py createsuperuser