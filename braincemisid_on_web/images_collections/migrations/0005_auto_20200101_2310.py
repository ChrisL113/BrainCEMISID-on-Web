# Generated by Django 2.2.7 on 2020-01-02 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images_collections', '0004_auto_20200101_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagesfromneuron',
            old_name='img64',
            new_name='image',
        ),
    ]
