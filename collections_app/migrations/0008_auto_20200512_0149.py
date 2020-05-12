# Generated by Django 3.0.5 on 2020-05-12 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0007_auto_20200512_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='coll_size',
            field=models.TextField(default='', help_text='Provide a statement about the size of the collection, including growth rate, etc.', max_length=1000),
        ),
    ]