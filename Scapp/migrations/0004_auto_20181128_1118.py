# Generated by Django 2.0.7 on 2018-11-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scapp', '0003_in_usa_out_usa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c',
            name='c_name',
            field=models.CharField(max_length=128),
        ),
    ]
