# Generated by Django 3.2.5 on 2021-08-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cf_rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
