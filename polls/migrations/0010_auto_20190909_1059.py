# Generated by Django 2.2.5 on 2019-09-09 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20190909_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breakdown',
            name='nUrl',
        ),
        migrations.AddField(
            model_name='breakdown',
            name='nUrlA',
            field=models.IntegerField(blank=True, db_column='nUrlA', null=True),
        ),
        migrations.AddField(
            model_name='breakdown',
            name='nUrlB',
            field=models.IntegerField(blank=True, db_column='nUrlB', null=True),
        ),
    ]
