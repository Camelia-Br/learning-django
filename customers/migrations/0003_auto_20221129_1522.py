# Generated by Django 3.2.16 on 2022-11-29 15:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('customers', '0002_person_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='person',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(
                blank=True,
                max_length=17,
                validators=[
                    django.core.validators.RegexValidator(
                        message='Phone number must be valid', regex='^(\\+\\d{1,3})?,?\\s?\\d{8,13}'
                    )
                ],
            ),
        ),
    ]
