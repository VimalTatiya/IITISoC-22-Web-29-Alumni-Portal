# Generated by Django 4.0.6 on 2022-07-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('finish_date', models.DateField()),
                ('finish_time', models.TimeField()),
                ('event_city', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('current_city', models.CharField(max_length=50)),
                ('yog', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=50)),
                ('status', models.TextField(max_length=400)),
                ('rollnum', models.CharField(max_length=15, primary_key='true', serialize=False)),
            ],
            options={
                'verbose_name': 'Info',
                'verbose_name_plural': 'Info',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadedBy', models.CharField(max_length=15, verbose_name='Name')),
                ('story_name', models.CharField(max_length=50)),
                ('story', models.TextField(max_length=1000)),
                ('magzine', models.FileField(upload_to='')),
                ('insti_update', models.TextField(max_length=1000)),
                ('achievements', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Story',
                'verbose_name_plural': 'Stories',
            },
        ),
    ]
