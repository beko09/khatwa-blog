# Generated by Django 3.0.8 on 2020-08-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200806_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='الوظيفة'),
        ),
    ]
