# Generated by Django 4.0 on 2021-12-23 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0003_alter_profile_date_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
