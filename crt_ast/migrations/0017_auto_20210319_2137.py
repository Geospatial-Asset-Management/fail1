# Generated by Django 3.1.3 on 2021-03-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crt_ast', '0016_asset_assetpropertyvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assettype',
            name='industry',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='assettypesymbol',
            name='symbol',
            field=models.ImageField(upload_to='symbol_img/'),
        ),
    ]