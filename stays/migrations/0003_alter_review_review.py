# Generated by Django 3.2.16 on 2023-07-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stays', '0002_alter_stay_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.CharField(max_length=5000),
        ),
    ]
