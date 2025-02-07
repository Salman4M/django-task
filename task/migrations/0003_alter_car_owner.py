# Generated by Django 5.0.6 on 2024-06-05 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0002_alter_car_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="owner",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cars",
                to="task.owner",
            ),
        ),
    ]
