# Generated by Django 2.0.5 on 2018-05-22 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_tehlikede'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='tehlikede',
            field=models.IntegerField(default=0),
        ),
    ]
