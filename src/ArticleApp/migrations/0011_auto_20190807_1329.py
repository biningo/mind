# Generated by Django 2.2.2 on 2019-08-07 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleApp', '0010_auto_20190805_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialtopic',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='content_html',
            field=models.TextField(default=0, verbose_name='翻译成html的内容'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='content_makedown',
            field=models.TextField(default=0, verbose_name='makedown内容'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialtopic',
            name='access_count',
            field=models.IntegerField(default=0, verbose_name='访问数量'),
        ),
    ]