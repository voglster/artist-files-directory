# Generated by Django 3.0.5 on 2020-05-07 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionsubjectcountry',
            name='coll_sub_country_url',
            field=models.URLField(default=django.utils.timezone.now, help_text='Provide VIAF permalink', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_name',
            field=models.CharField(blank=True, help_text='Use for formal name of a collection or to describe a collection with special characteristics, for example The Nettie Wheeler Artist Files on Native American Artists', max_length=255),
        ),
        migrations.AlterField(
            model_name='collectionsubjectcountry',
            name='coll_sub_country',
            field=models.CharField(help_text='Use preferred VIAF form of name', max_length=100),
        ),
    ]
