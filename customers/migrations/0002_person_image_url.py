# Generated by Django 3.2.16 on 2022-11-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image_url',
            field=models.ImageField(default='cami.jpg', upload_to=None),
        ),
    ]
