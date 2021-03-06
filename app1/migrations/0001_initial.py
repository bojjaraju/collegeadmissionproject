# Generated by Django 3.1.2 on 2020-10-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('sname', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('sfathername', models.CharField(max_length=25)),
                ('sdob', models.DateField(auto_now=True)),
                ('saadharno', models.IntegerField()),
                ('smothername', models.CharField(max_length=25)),
                ('sschoolname', models.CharField(max_length=50)),
                ('sgrade', models.FloatField()),
                ('scollegename', models.CharField(max_length=50)),
                ('smarks', models.IntegerField()),
                ('shouseno', models.IntegerField()),
                ('scolonyname', models.CharField(max_length=50)),
                ('scityname', models.CharField(max_length=50)),
                ('sdistrictname', models.CharField(max_length=50)),
                ('smandalname', models.CharField(max_length=50)),
                ('sphonenumber', models.IntegerField()),
                ('sgmail', models.EmailField(max_length=254)),
            ],
        ),
    ]
