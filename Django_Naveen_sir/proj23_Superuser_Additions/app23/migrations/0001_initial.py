# Generated by Django 2.1.7 on 2019-03-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contactno', models.ImageField(upload_to='')),
                ('designation', models.CharField(max_length=30)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]