# Generated by Django 3.0.5 on 2020-07-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0026_auto_20200727_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='cat_system',
            field=models.ManyToManyField(blank=True, help_text='Add systems used for cataloging artist files collection. Hold down “Control” or “Command” to select more than one value.<br /><a href="/collections/cataloging_systems" target="blank">Create or update terms</a>, then reload to this page to use.', related_name='collections', to='collections_app.CollectionCatSystem', verbose_name='Cataloging Systems'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='service',
            field=models.ManyToManyField(blank=True, help_text='Add reference services offered. Hold down “Control” or “Command” to select more than one value.<br /><a href="/collections/reference_services" target="blank">Create or update terms</a>, then reload to this page to use.', related_name='collections', to='collections_app.CollectionService', verbose_name='Reference Services'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='spec_format',
            field=models.ManyToManyField(blank=True, help_text='Add special formats contained in the collection, either analog or digital. Hold down “Control” or “Command” to select more than one value.<br /><a href="/collections/special_formats" target="blank">Create or update terms</a>, then reload to this page to use.', related_name='collections', to='collections_app.CollectionSpecialFormat', verbose_name='Special Formats'),
        ),
    ]
