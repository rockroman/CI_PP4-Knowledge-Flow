# Generated by Django 3.2.16 on 2023-01-23 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteusers', '0002_remove_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.URLField(default='https://www.google.com/', max_length=100),
        ),
    ]
