# Generated by Django 3.0.5 on 2020-07-24 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0023_collection_consortium_website'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='consortium_website',
            new_name='consortium_url',
        ),
    ]
