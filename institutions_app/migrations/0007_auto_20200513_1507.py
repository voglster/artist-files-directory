# Generated by Django 3.0.5 on 2020-05-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions_app', '0006_auto_20200513_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutiontype',
            name='type_name',
            field=models.CharField(max_length=100, verbose_name='Type'),
        ),
    ]
