# Generated by Django 3.2.13 on 2022-06-07 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MenuHum', '0005_rename_active_menu_hum_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_hum',
            name='imagen',
            field=models.ImageField(null=True, upload_to='producto'),
        ),
    ]