# Generated by Django 2.2.4 on 2019-08-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190816_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='default', max_length=140),
        ),
    ]