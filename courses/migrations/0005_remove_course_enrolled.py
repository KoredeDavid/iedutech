# Generated by Django 3.0.5 on 2020-11-29 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_enrolled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='enrolled',
        ),
    ]
