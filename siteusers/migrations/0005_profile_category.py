# Generated by Django 3.2.16 on 2023-01-24 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('siteusers', '0004_profile_linkedin_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='category',
            field=models.ManyToManyField(related_name='user_learning_categoy', to='categories.LearningCategory'),
        ),
    ]
