# Generated by Django 3.2.7 on 2021-09-30 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='emid',
        ),
    ]
