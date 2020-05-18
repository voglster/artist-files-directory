# Generated by Django 3.0.5 on 2020-05-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0029_auto_20200518_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectionsubjecttopic',
            old_name='description',
            new_name='notes',
        ),
        migrations.AlterField(
            model_name='collectionsubjecttopic',
            name='coll_sub_topic',
            field=models.CharField(help_text='Use term from <a href="http://id.loc.gov/authorities/subjects.html" target="_blank">LCSH </a> or other authority.', max_length=100, verbose_name='Subject: Topic'),
        ),
    ]
