# Generated by Django 2.2.5 on 2019-09-05 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20190905_1516'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
