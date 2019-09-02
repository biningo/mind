# Generated by Django 2.2.1 on 2019-08-23 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleApp', '0015_auto_20190820_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialtopic',
            name='articles',
        ),
        migrations.AlterField(
            model_name='article',
            name='topic',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ArticleApp.SpecialTopic', verbose_name='专题'),
        ),
    ]
