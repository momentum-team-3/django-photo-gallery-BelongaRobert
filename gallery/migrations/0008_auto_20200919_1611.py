# Generated by Django 3.1.1 on 2020-09-19 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0007_auto_20200917_2320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='albums',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='comments',
        ),
        migrations.AddField(
            model_name='photo',
            name='albums_in',
            field=models.ManyToManyField(blank=True, related_name='photos', to='gallery.Album'),
        ),
        migrations.AddField(
            model_name='photo',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='default_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.photo'),
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='album',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='album',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.TextField(max_length=150),
        ),
    ]