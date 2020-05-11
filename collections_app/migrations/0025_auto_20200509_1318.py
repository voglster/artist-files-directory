# Generated by Django 3.0.5 on 2020-05-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0024_auto_20200509_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='coll_loc_city',
            field=models.CharField(help_text='Important for providing access to collections located in specific cities.', max_length=255),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_loc_country',
            field=models.CharField(help_text='Important for providing access to collections located in specific countries.', max_length=255),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_loc_state_prov',
            field=models.CharField(help_text='Important for providing access to collections located in specific states or provinces.', max_length=255),
        ),
    ]
