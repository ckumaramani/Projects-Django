# Generated by Django 2.1.7 on 2019-03-09 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app28', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useername', models.CharField(max_length=30)),
                ('fb', models.TextField()),
            ],
        ),
    ]