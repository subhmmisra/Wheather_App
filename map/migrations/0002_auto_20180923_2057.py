# Generated by Django 2.1.1 on 2018-09-23 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='location',
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]