# Generated by Django 3.2.16 on 2023-01-01 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteusers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
