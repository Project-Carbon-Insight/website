# Generated by Django 4.2.4 on 2024-09-01 04:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("state_data", "0008_alter_energydata_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="energydata",
            name="gdp",
            field=models.CharField(max_length=20),
        ),
    ]
