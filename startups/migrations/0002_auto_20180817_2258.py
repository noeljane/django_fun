# Generated by Django 2.0.6 on 2018-08-17 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='photo_attribute',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='photo_photographer',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='photo_profile_link',
            field=models.TextField(blank=True),
        ),
    ]
