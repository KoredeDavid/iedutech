# Generated by Django 3.0.5 on 2020-11-29 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20201127_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='enrolled',
            field=models.BooleanField(default=False),
        ),
    ]
