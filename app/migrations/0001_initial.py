# Generated by Django 4.2.5 on 2023-09-11 19:33

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('external_api_key', models.CharField(max_length=500, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='username')),
                ('hashed_password', models.CharField(max_length=50, verbose_name='password')),
                ('bio', models.CharField(max_length=500, verbose_name='bio')),
                ('display_name', models.CharField(max_length=100)),
                ('favorite_show', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.anime')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_rating', models.IntegerField(validators=[app.models.validate_rating])),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_name', models.CharField(max_length=100, unique=True)),
                ('summary', models.CharField(max_length=225)),
                ('episodes', models.ManyToManyField(to='app.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.anime')),
            ],
        ),
    ]
