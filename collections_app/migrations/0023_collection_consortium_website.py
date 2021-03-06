# Generated by Django 3.0.5 on 2020-07-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0022_auto_20200724_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='consortium_website',
            field=models.URLField(blank=True, help_text='Add website for consortial/shared collection.', max_length=255, verbose_name='Website'),
        ),
    ]
