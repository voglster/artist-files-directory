# Generated by Django 3.0.5 on 2020-06-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0021_auto_20200601_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='telephone_pref',
            field=models.BooleanField(blank=True, verbose_name='Is telephone a preferred contact?'),
        ),
    ]
