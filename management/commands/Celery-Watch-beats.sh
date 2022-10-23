docker exec -it django_fintech_enterprise_container celery -A fintechengine  beat -l INFO --logfile=celery.log
