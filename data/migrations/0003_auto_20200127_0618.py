# Generated by Django 3.0.2 on 2020-01-27 06:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0002_auto_20200127_0615'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserStatus',
            new_name='UserStatu',
        ),
    ]