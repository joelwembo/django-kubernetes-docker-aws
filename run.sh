echo 'Compiling the engine...'

echo 'Performing Migrations...'

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000
