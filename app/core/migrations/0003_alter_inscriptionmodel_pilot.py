# Generated by Django 4.1.2 on 2022-11-05 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_inscriptionmodel_copilot_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscriptionmodel',
            name='pilot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscription_pilot', to='core.competitormodel'),
        ),
    ]
