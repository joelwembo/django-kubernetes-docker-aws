FROM python:3.9.10-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY . .
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

RUN python /src/wheremyfile/finbo.py

EXPOSE 8000

# gunicorn
#CMD ["gunicorn", "--config", "gunicorn-cfg.py", "fintechengine.wsgi"]
#RUN gunicorn fintechengine.wsgi:application --bind 0.0.0.0:8585