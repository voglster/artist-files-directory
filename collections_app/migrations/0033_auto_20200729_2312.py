# Generated by Django 3.0.5 on 2020-07-29 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0032_auto_20200729_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='quote',
            field=models.TextField(blank=True, help_text='Provide a pithy quote or tagline for the collection. A quote makes the entry look better, besides rounding out the description. The system automatically adds quotes.', max_length=500, verbose_name='Quote'),
        ),
    ]
