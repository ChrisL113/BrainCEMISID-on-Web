# Generated by Django 3.0.2 on 2020-03-25 01:50

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0004_auto_20200302_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='episodic_memoryproto',
            fields=[
                ('brain_episodic_memory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='brain.brain')),
                ('index_ready_to_learn', models.IntegerField()),
                ('clack', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='EpisodicMemNeuron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_knowledge', models.BooleanField()),
                ('knowledge', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_bip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RecognizedIndexesEpisodicMemory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_recognized', models.IntegerField()),
                ('episodic_memory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='index_recognize', to='brain.episodic_memoryproto')),
            ],
        ),
    ]