# Generated by Django 3.1.7 on 2021-03-14 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crt_ast', '0014_auto_20210314_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetpropertyvalue',
            name='asset',
        ),
        migrations.RemoveField(
            model_name='assetpropertyvalue',
            name='property',
        ),
        migrations.DeleteModel(
            name='Asset',
        ),
        migrations.DeleteModel(
            name='AssetPropertyValue',
        ),
    ]