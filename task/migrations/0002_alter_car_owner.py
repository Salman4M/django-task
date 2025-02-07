# Generated by Django 5.0.6 on 2024-06-05 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cars",
                to="task.owner",
            ),
        ),
    ]
