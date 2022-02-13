# Generated by Django 4.0.2 on 2022-02-13 22:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('task', models.CharField(default=' ', max_length=30)),
                ('description', models.TextField()),
                ('emotion', models.CharField(choices=[('Very Happy', 'Very Happy'), ('Happy', 'Happy'), ('Content', 'Content'), ('Dissatisfied', 'Dissatisfied'), ('Extremely Dissatisfied', 'Extremely Dissatisfied')], max_length=30)),
                ('hours_worked', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]