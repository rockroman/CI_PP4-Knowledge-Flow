# Generated by Django 3.2.16 on 2023-01-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_learningcategory_start_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningcategory',
            name='importance_of_category',
            field=models.TextField(null=True),
        ),
    ]
