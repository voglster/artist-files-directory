# Generated by Django 3.0.5 on 2020-05-08 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0019_auto_20200508_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='coll_name',
            field=models.CharField(default='General Collection', help_text='Use "General Collection" if describing all files as one combined entry; otherwise, create a separate entry for each formally named collection or collection with special characteristics, for example "The Nettie Wheeler Artist Files on Native American Artists."', max_length=255),
        ),
    ]
