# Generated by Django 2.1.7 on 2019-03-18 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arjun',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('designatoin', models.CharField(max_length=30)),
                ('contactno', models.IntegerField()),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
