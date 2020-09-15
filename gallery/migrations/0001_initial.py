# Generated by Django 3.1.1 on 2020-09-15 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('public', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=35)),
                ('image', models.FileField(upload_to='images/')),
                ('summary', models.TextField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('albums', models.ManyToManyField(blank=True, to='gallery.Album')),
            ],
        ),
    ]
