# Generated by Django 3.0.5 on 2020-05-13 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0010_auto_20200513_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='coll_access',
            field=models.TextField(help_text='Add policies and procedures relating to how researchers access and use the collection.', max_length=1000, verbose_name='Access and Use'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_cat_system',
            field=models.ManyToManyField(help_text='Add systems used for cataloging artist files collection. Create a new system if there is not a fit.', related_name='Collection', to='collections_app.CollectionCatSystem', verbose_name='Cataloging Systems'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_description',
            field=models.TextField(help_text='Provide a general description of the collection, including such aspects as history and provenance. Also use this field for general notes about the collection.', max_length=1000, verbose_name='General Description'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_dig_access',
            field=models.URLField(blank=True, help_text='Provide URL for accessing digital collection.', max_length=255, verbose_name='Digital Project Website'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_dig_projects',
            field=models.TextField(blank=True, help_text='Describe digital projects, either completed or planned.', max_length=1000, verbose_name='Digital Projects'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_image',
            field=models.ForeignKey(blank=True, help_text='Upload images showing example material from files and/or storage systems in use.', null=True, on_delete=django.db.models.deletion.CASCADE, to='collections_app.CollectionImage', verbose_name='Collection Image(s)'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_name',
            field=models.CharField(default='General Collection', help_text='Use "General Collection" if describing all files as one combined entry; otherwise, create a separate entry for each formally named collection or collection with special characteristics, for example "The Nettie Wheeler Artist Files on Native American Artists."', max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_services',
            field=models.ManyToManyField(help_text='Add reference services offered. Create a new service if there is not a fit.', related_name='Collection', to='collections_app.CollectionService', verbose_name='Services'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_size',
            field=models.TextField(default='', help_text='Provide a statement about the size of the collection, including growth rate, etc. Use whatever measurement terms are relevant.', max_length=1000, verbose_name='Size'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_spec_format',
            field=models.ManyToManyField(blank=True, help_text='Add special formats contained in the collection, either analog or digital. Create a new type if there is not a fit.', related_name='Collection', to='collections_app.CollectionSpecialFormat', verbose_name='Special Formats'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_subject_city',
            field=models.ManyToManyField(blank=True, help_text='Add cities that are subject focuses of the files', related_name='Collection', to='collections_app.CollectionSubjectCity', verbose_name='Subject - Cities'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_subject_country',
            field=models.ManyToManyField(blank=True, help_text='Add countries that are subject focuses of the files.', related_name='Collection', to='collections_app.CollectionSubjectCountry', verbose_name='Subject - Countries'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_subject_county',
            field=models.ManyToManyField(blank=True, help_text='Add counties that are subject focuses of the files.', related_name='Collection', to='collections_app.CollectionSubjectCounty', verbose_name='Subject - Counties'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_subject_geo_area',
            field=models.ManyToManyField(blank=True, help_text='Add geographic areas, such as West U.S. that are subject focuses of the files.', related_name='Collection', to='collections_app.CollectionSubjectGeoArea', verbose_name='Subject - Geographic Areas'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_subject_name',
            field=models.ManyToManyField(blank=True, help_text='Add personal and institutional names that are subjects of the collection.', related_name='Collection', to='collections_app.CollectionSubjectName', verbose_name='Subject - Names'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_subject_state_prov',
            field=models.ManyToManyField(blank=True, help_text='Add states or provinces that are subject focuses of the files.', related_name='Collection', to='collections_app.CollectionSubjectStateProv', verbose_name='Subject - States and Provinces'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_subject_topic',
            field=models.ManyToManyField(blank=True, help_text='Add topical terms that are the subject focuses of the files.', related_name='Collection', to='collections_app.CollectionSubjectTopic', verbose_name='Subject - Topics'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_website',
            field=models.URLField(blank=True, help_text='Add website describing or providing access to the collection.', max_length=255, verbose_name='Website'),
        ),
    ]
