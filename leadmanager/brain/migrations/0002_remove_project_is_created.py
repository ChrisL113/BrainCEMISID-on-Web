# Generated by Django 2.2.5 on 2019-10-26 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='is_created',
        ),
    ]