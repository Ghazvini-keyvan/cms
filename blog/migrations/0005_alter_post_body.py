# Generated by Django 3.2.6 on 2021-08-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210819_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=350, verbose_name='body'),
        ),
    ]