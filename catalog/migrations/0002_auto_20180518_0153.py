# Generated by Django 2.0.5 on 2018-05-17 22:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Profile',
        ),
    ]
