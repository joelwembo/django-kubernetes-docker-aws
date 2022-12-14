# Generated by Django 4.0.4 on 2022-11-05 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0007_remove_book_authors_remove_book_publisher_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
