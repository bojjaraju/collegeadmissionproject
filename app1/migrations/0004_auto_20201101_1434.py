# Generated by Django 3.1.2 on 2020-11-01 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20201101_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='board',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='code',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='degreegroup',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='intergroup',
            field=models.BooleanField(),
        ),
    ]
