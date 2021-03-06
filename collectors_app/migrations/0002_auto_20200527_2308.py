# Generated by Django 3.0.5 on 2020-05-27 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='inst_type',
            field=models.ManyToManyField(blank=True, help_text='Choose all types that are relevant. Create a new type if there is not a fit.', related_name='Collector', to='collectors_app.InstitutionType', verbose_name='Institution Types'),
        ),
        migrations.AlterField(
            model_name='collector',
            name='person_type',
            field=models.ManyToManyField(blank=True, help_text='Choose all types that are relevant. Create new type if there is not a fit.', related_name='Collector', to='collectors_app.PersonType', verbose_name='Person Types'),
        ),
    ]
