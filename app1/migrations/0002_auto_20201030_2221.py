# Generated by Django 3.1.2 on 2020-10-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cbse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='female',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='male',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='ssc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='transgender',
            field=models.BooleanField(default=False),
        ),
    ]
