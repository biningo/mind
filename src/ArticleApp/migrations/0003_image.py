# Generated by Django 2.2.2 on 2019-07-09 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleApp', '0002_article_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ImageFile', models.ImageField(upload_to='')),
            ],
        ),
    ]