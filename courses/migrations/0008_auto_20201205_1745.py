# Generated by Django 3.0.5 on 2020-12-05 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
