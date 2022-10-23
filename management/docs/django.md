# Creating App Inside Apps Parent app directory

 1. Inside apps folder create a new folder flight as app

 2. python manage.py startapp flight apps/flight

 3. inside flight On apps.py

 from django.apps import AppConfig


class FlightConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.flight'


