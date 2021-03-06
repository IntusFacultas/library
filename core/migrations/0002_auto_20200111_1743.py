# Generated by Django 3.0.2 on 2020-01-11 22:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='checked_out',
            field=models.BooleanField(default=False, verbose_name='Checked Out'),
        ),
        migrations.AddField(
            model_name='book',
            name='date_checked_out',
            field=models.DateField(default=datetime.datetime(2020, 1, 11, 22, 43, 36, 703898, tzinfo=utc), verbose_name='Date Checked Out'),
            preserve_default=False,
        ),
    ]
