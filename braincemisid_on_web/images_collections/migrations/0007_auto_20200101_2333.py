# Generated by Django 2.2.7 on 2020-01-02 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_collections', '0006_auto_20200101_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesfromneuron',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
