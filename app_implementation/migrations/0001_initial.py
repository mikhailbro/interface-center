# Generated by Django 3.2.10 on 2021-12-31 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_interface', '0013_auto_20211231_1854'),
        ('app_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Implementation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_basepath', models.CharField(default='', max_length=100)),
                ('implementation_counter', models.PositiveIntegerField(default=1)),
                ('implementation_type', models.CharField(choices=[('WEB_SERVICE', 'Web Service'), ('API', 'Api'), ('QUEUE', 'Queue')], default='API', max_length=20)),
                ('interface', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_interface.interface')),
                ('provider', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='app_application.application')),
            ],
        ),
    ]