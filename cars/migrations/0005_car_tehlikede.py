# Generated by Django 2.0.5 on 2018-05-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_plaka'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='tehlikede',
            field=models.BooleanField(default=False),
        ),
    ]