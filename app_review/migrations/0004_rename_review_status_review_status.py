# Generated by Django 3.2.10 on 2022-05-05 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_review', '0003_auto_20220121_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_status',
            new_name='status',
        ),
    ]
