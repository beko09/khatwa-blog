# Generated by Django 3.0.8 on 2020-08-09 16:38

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200807_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=mdeditor.fields.MDTextField(),
        ),
    ]