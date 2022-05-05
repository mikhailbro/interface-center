# Generated by Django 3.2.10 on 2022-05-05 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_implementation', '0006_alter_implementation_implementation_counter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='implementation',
            old_name='provider_basepath',
            new_name='delivery_address',
        ),
        migrations.RenameField(
            model_name='implementation',
            old_name='implementation_counter',
            new_name='provider_counter',
        ),
        migrations.RenameField(
            model_name='implementation',
            old_name='implementation_type',
            new_name='technology_type',
        ),
        migrations.AddField(
            model_name='implementation',
            name='artefact_url',
            field=models.URLField(blank=True, default=None, null=True, verbose_name='Artefact URL'),
        ),
    ]