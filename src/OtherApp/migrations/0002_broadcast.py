# Generated by Django 2.2.2 on 2019-08-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OtherApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadCast',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
    ]
