# Generated by Django 3.1.7 on 2021-03-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crt_ast', '0021_auto_20210320_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='markercolor',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='markersymbol',
            field=models.CharField(max_length=1, null=True),
        ),
    ]