# Generated by Django 4.2 on 2023-04-27 19:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("university", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="date_of_birthday",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name="group",
            name="group_name",
            field=models.CharField(max_length=10),
        ),
    ]
