# Generated by Django 3.0.5 on 2020-05-07 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons_app', '0007_auto_20200507_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='pers_email',
            new_name='per_email',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='pers_tel',
            new_name='per_tel',
        ),
    ]
