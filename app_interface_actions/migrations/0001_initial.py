# Generated by Django 3.2.10 on 2022-01-20 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interface_Actions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface_id', models.CharField(default='wird vom Tool vergeben', max_length=31, verbose_name='Interface ID')),
                ('name', models.CharField(max_length=100)),
                ('version', models.PositiveIntegerField(default=1)),
                ('description', models.TextField(default='', max_length=500)),
                ('contract_description', models.URLField(blank=True, default=None, null=True, verbose_name='Interface Contract URL')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('production_start_at', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
