# Generated by Django 3.1.7 on 2021-03-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crt_ast', '0023_auto_20210321_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='markercolor',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
