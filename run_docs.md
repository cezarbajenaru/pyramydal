basic stuff:
###
Django admin password
plasticmemory
plastic
bajenarucezar@gmail.com
###


####################
django-admin --version
#############################

###################
Check users existing
python manage.py shell

from django.contrib.auth.models import User
User.objects.values("username", "is_staff", "is_superuser")
######################

############# 
If you want to fix an existing user:
python manage.py shell

```
from django.contrib.auth.models import User

u = User.objects.get(username="YOUR_USERNAME")
u.is_staff = True
u.is_superuser = True
u.set_password("newpassword")
u.save()

```
########################


This command is only for creation ( runs only once):
python3 -m venv .venv
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
This is for activation of the venv. Run everytime you do mods on the project
plasticmemory@~/projects/pyramydal/backend[main]
$ source ./.venv/bin/activate
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```
Before any Django command:

cd pyramydal          # directory with manage.py
source .venv/bin/activate
python manage.py <command>


This rule applies to:

runserver

migrate

makemigrations

createsuperuser

shell
```


Things are installed in venv

Ensure you are in venv


Django uses SQLite by default (fine for now).
Run:
python manage.py migrate  # this initiates SQ liste as default

Create admin user:
python manage.py createsuperuser
Write the user

Run the server
python manage.py runserver

Use this adress:
http://127.0.0.1:8000/admin/

Go to: 
(.venv) plasticmemory@~/projects/pyramydal/backend/pyramydal[main]
$ python3 manage.py runserver


#################################
#postgresql install

sudo apt update
sudo apt install postgresql postgresql-contrib -y
psql --version
sudo -u postgres psql   # to login as user
# run these under the user login in postgresql

```
CREATE DATABASE pyramydal;
CREATE USER pyramydal_user WITH PASSWORD 'pyramydal_pass';
ALTER ROLE pyramydal_user SET client_encoding TO 'utf8';
ALTER ROLE pyramydal_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE pyramydal_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE pyramydal TO pyramydal_user;
```
\q to quit

check version
python -c "import psycopg; print(psycopg.__version__)"

Go to : config/settings.py


DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "pyramydal",
        "USER": "pyramydal_user",
        "PASSWORD": "pyramydal_pass",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


Check connection via Django Shell

python manage.py shell
