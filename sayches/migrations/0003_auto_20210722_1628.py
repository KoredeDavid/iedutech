# Generated by Django 3.0.5 on 2021-07-22 15:28

from django.db import migrations, models
import sayches.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sayches', '0002_auto_20210722_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pop',
            name='image',
            field=models.FileField(upload_to='bla/', validators=[sayches.validators.mime_validator]),
        ),
    ]
