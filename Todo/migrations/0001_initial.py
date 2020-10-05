# Generated by Django 3.0.7 on 2020-08-20 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('msg', models.TextField()),
                ('slug', models.CharField(max_length=255)),
                ('img_url', models.CharField(max_length=3056)),
            ],
        ),
    ]
