# Generated by Django 4.0.4 on 2022-08-09 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0005_author_publisher_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='headshot',
        ),
    ]