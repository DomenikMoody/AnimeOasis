# Generated by Django 4.2.5 on 2023-09-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='bio'),
        ),
    ]