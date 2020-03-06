# Generated by Django 2.1.5 on 2019-02-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('designation', models.CharField(max_length=20)),
                ('shift', models.CharField(max_length=20)),
                ('loans', models.CharField(max_length=50)),
            ],
        ),
    ]
