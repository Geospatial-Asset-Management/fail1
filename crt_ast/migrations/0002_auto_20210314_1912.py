# Generated by Django 3.1.3 on 2021-03-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crt_ast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assettype',
            name='industry',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='assettypeproperty',
            name='description',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='assettype',
            name='description',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='assettype',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='assettypeproperty',
            name='dtype',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
