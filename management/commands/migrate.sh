#python3 manage.py makemigrations
#python3 manage.py migrate

echo 'Migration Operation Completed , Please Check the logs status'

docker exec -it django_fintech_enterprise_container python manage.py makemigrations
docker exec -it django_fintech_enterprise_container python manage.py migrate