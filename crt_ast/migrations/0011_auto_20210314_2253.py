# Generated by Django 3.1.7 on 2021-03-14 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crt_ast', '0010_seniorstaff_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=75)),
                ('office_location', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('description', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='staff',
            name='reports_to',
        ),
        migrations.DeleteModel(
            name='SeniorStaff',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]