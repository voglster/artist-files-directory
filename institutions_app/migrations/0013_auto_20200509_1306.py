# Generated by Django 3.0.5 on 2020-05-09 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0023_auto_20200509_0012'),
        ('institutions_app', '0012_auto_20200509_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='inst_collection',
            field=models.ForeignKey(help_text='Create an artist files collection and provide details. Multiple collections allowed and encouraged. Create a separate entry for each formally named collection or collection with special characteristics, for example "The Nettie Wheeler Artist Files on Native American Artists."', on_delete=django.db.models.deletion.CASCADE, to='collections_app.Collection'),
        ),
    ]
