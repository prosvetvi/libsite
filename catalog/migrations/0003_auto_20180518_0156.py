# Generated by Django 2.0.5 on 2018-05-17 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180518_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bookreading',
            name='date_last_read',
            field=models.DateTimeField(verbose_name='time last reading'),
        ),
    ]