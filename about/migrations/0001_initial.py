# Generated by Django 3.0.8 on 2020-08-05 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=50)),
                ('about', models.TextField()),
            ],
        ),
    ]
