# Generated by Django 3.0.6 on 2021-05-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_moviespider_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='full/'),
        ),
    ]
