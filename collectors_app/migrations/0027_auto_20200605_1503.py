# Generated by Django 3.0.5 on 2020-06-05 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0026_auto_20200603_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='collector',
            name='inst_dealer',
            field=models.BooleanField(blank=True, default=False, verbose_name='Is this a dealer?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='collector',
            name='inst_main_name',
            field=models.CharField(blank=True, help_text='If an institutional collection, provide main institution name.', max_length=255, verbose_name='Institution/Dealer Main Name'),
        ),
        migrations.AlterField(
            model_name='collector',
            name='inst_sub_name',
            field=models.CharField(blank=True, help_text='If an institutional collection, provide name of department, division, etc., responsible for artist files.', max_length=255, verbose_name='Institution/Dealer Secondary Name'),
        ),
    ]
