# Generated by Django 3.1.1 on 2020-09-29 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0027_auto_20200929_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='albums_in',
        ),
        migrations.AddField(
            model_name='photo',
            name='albums',
            field=models.ManyToManyField(related_name='photos', to='gallery.Album'),
        ),
    ]
