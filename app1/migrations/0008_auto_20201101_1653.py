# Generated by Django 3.1.2 on 2020-11-01 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_studentmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sphonenumber',
            field=models.CharField(max_length=20),
        ),
    ]
