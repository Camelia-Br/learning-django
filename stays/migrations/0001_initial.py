# Generated by Django 3.2.16 on 2022-12-12 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0004_alter_pet_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.person')),
                ('pets', models.ManyToManyField(to='customers.Pet')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.provider')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=500)),
                ('rating', models.CharField(max_length=5)),
                ('stay', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stays.stay')),
            ],
        ),
    ]
