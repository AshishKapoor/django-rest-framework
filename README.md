# django-rest-framework backend

### Deployment References
1. Gunicorn - https://docs.gunicorn.org/en/stable/configure.html

## For Migration to Postgres
```
$ pip install psycopg2
```

## Run locally

http://0.0.0.0:8000

## Some useful commands
```
Django-admin startproject <project-name> 

python manage.py runserver (can be put in config)

python manage.py startapp <app-name>

# add to database
python manage.py migrate

# create migration only
python manage.py makemigrations

pip3 install djangorestframework

python manage.py createsuperuser

# generate requirements.txt file
pip freeze > requirements.txt

```