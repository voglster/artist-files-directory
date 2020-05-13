# Generated by Django 3.0.5 on 2020-05-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0011_auto_20200513_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='coll_loc_city',
            field=models.CharField(help_text='Important for providing access to collections located in specific cities.', max_length=255, verbose_name='Collection Location - City'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_loc_country',
            field=models.CharField(help_text='Important for providing access to collections located in specific countries.', max_length=255, verbose_name='Collection Location - Country'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_loc_state_prov',
            field=models.CharField(help_text='Important for providing access to collections located in specific states or provinces.', max_length=255, verbose_name='Collection Location - State/Province'),
        ),
    ]
