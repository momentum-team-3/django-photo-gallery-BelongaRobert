# Generated by Django 3.1.1 on 2020-09-20 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0018_auto_20200920_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='image',
            new_name='media',
        ),
    ]