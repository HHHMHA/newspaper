# Generated by Django 3.1.2 on 2020-10-07 21:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0006_auto_20201008_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]