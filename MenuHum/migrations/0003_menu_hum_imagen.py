# Generated by Django 3.2.13 on 2022-06-05 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MenuHum', '0002_menu_hum_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_hum',
            name='imagen',
            field=models.ImageField(null=True, upload_to='producto'),
        ),
    ]