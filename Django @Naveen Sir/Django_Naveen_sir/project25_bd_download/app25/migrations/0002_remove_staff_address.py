# Generated by Django 2.1.7 on 2019-03-03 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app25', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='Address',
        ),
    ]