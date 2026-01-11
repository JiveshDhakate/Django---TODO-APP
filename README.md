# Create venv
python -m venv env

# Create Django Project     
django-admin startproject todo_main . 

# Create Super User
 ### Step 1- Migrate
            python manage.py migrate
 ### Step 2 - Create Superuser
            python manage.py createsuperuser

# Create APP
    Todo APP - python manage.py startapp todo
    Step 1- Create Model
            Model Contains backend
            class Task tell us how its stote 
    Step 2- Register it in admin.py
    Step 3 - Create and Apply Migartions
             python manage.py makemigrations
             python manage.py migrate
