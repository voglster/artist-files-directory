# Generated by Django 3.0.5 on 2020-06-01 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0012_auto_20200601_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='other_contact',
            field=models.CharField(blank=True, help_text='Provide other form of contact.', max_length=255, verbose_name='Other Contact'),
        ),
    ]
