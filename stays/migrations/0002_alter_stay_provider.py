# Generated by Django 3.2.16 on 2023-02-10 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_alter_pet_name'),
        ('stays', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stay',
            name='provider',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='stays', to='customers.provider'
            ),
        ),
    ]
