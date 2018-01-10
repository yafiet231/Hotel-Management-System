# Generated by Django 2.0 on 2018-01-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20180109_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='room',
            name='staff',
        ),
        migrations.AlterField(
            model_name='room',
            name='availability',
            field=models.BooleanField(default=0),
        ),
    ]
