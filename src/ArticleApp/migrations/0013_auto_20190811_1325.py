# Generated by Django 2.2.2 on 2019-08-11 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleApp', '0012_delete_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='father_comment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ArticleApp.ArticleComment', verbose_name='回复'),
        ),
    ]
