python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

psql postgres

create role MyNewUserName with login password 'mysecurepassword';
alter role MyNewUserName superuser;
\q

psql postgres -U MyNewUserName
create database foodstah_db;
\q

# at this point please create a file with the name ".env" in the same directory as settings.py
# fill out with the info i'll send you on slack, and put in the DB username + password you set previously

cd foodstah

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py createsuperuser

# now you can runserver :)