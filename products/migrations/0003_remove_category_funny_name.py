# Generated by Django 3.2.5 on 2021-07-27 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210724_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='funny_name',
        ),
    ]