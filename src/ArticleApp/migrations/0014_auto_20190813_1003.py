# Generated by Django 2.2.2 on 2019-08-13 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleApp', '0013_auto_20190811_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建或者修改时间'),
        ),
    ]