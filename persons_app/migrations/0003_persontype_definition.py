# Generated by Django 3.0.5 on 2020-05-01 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons_app', '0002_auto_20200501_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='persontype',
            name='definition',
            field=models.TextField(default='', max_length=500),
        ),
    ]
