# Generated by Django 4.1.5 on 2023-03-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='list_name',
            fields=[
                ('list_id', models.IntegerField(primary_key=True, serialize=False)),
                ('list_name', models.CharField(max_length=100)),
                ('list_location', models.CharField(max_length=400)),
                ('list_quality_expiry', models.DateTimeField()),
                ('list_price', models.FloatField(default=0)),
                ('list_rating', models.FloatField(default=3.0)),
                ('list_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ver',
            fields=[
                ('list_id', models.IntegerField(primary_key=True, serialize=False)),
                ('list_name', models.CharField(max_length=100)),
                ('list_location', models.CharField(max_length=400)),
                ('list_price', models.FloatField(default=0)),
                ('list_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
