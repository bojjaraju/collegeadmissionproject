# Generated by Django 3.1.2 on 2020-11-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20201101_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentmessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sfname', models.CharField(max_length=25)),
                ('slname', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=25)),
                ('message', models.TextField(max_length=25)),
            ],
        ),
    ]
