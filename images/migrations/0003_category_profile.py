# Generated by Django 3.1 on 2023-04-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20230408_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='profile',
            field=models.CharField(default='', max_length=500),
        ),
    ]
