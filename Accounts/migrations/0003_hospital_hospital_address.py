# Generated by Django 3.2 on 2021-05-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_auto_20210501_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='hospital_address',
            field=models.TextField(blank=True),
        ),
    ]
