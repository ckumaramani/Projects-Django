# Generated by Django 2.1.7 on 2019-03-14 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArjunStaff',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('contactno', models.IntegerField()),
                ('designation', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
