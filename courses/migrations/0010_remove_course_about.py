# Generated by Django 3.2.6 on 2021-11-29 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20211129_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='about',
        ),
    ]
