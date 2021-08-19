# Generated by Django 3.2.6 on 2021-08-19 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=250, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='post/', verbose_name='thumbnail'),
        ),
    ]
