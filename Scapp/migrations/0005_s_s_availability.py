# Generated by Django 2.0.7 on 2018-11-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scapp', '0004_auto_20181128_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='s',
            name='s_availability',
            field=models.BooleanField(default=True),
        ),
    ]