# Generated by Django 2.2.1 on 2019-08-25 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalSpaceApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TimeLines',
            new_name='Mood',
        ),
    ]