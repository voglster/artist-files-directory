# Generated by Django 3.0.5 on 2020-05-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions_app', '0014_auto_20200509_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='inst_type',
            field=models.ManyToManyField(default='', help_text='Choose all types that are relevant. Create type if there is not a fit.', related_name='Institution', to='institutions_app.InstitutionType'),
        ),
    ]
