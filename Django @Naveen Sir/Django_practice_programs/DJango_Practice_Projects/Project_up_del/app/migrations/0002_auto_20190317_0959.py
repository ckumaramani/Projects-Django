# Generated by Django 2.1.7 on 2019-03-17 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='contactno',
            field=models.IntegerField(),
        ),
    ]