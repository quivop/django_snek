# Generated by Django 2.0.2 on 2018-03-08 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fic', '0002_auto_20180307_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ficlink',
            name='fanfic',
        ),
        migrations.DeleteModel(
            name='Fanfic',
        ),
        migrations.DeleteModel(
            name='FicLink',
        ),
    ]
