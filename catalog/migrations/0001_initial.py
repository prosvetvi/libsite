# Generated by Django 2.0.5 on 2018-05-21 02:45

import catalog.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('patronymic', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2018, 5, 21, 2, 45, 0, 85829, tzinfo=utc), verbose_name='date published')),
                ('read_date', models.DateTimeField(verbose_name='date reading')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('file', models.FileField(blank=True, null=True, upload_to='', validators=[catalog.models.file_size])),
                ('can_download', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Author')),
            ],
        ),
        migrations.CreateModel(
            name='BookReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_last_read', models.DateTimeField(verbose_name='time last reading')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bookreading',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Profile'),
        ),
    ]
