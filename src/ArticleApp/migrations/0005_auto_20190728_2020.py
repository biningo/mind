# Generated by Django 2.2.2 on 2019-07-28 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleApp', '0004_auto_20190714_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='father_comment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ArticleApp.ArticleComment', verbose_name='回复'),
        ),
    ]
