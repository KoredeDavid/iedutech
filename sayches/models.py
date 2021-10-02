from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from sayches.validators import max_word, mime_validator


class Pop(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(validators=[max_word])
    image = models.FileField(
        validators=[mime_validator, FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
        upload_to='bla/',
    )

    def __str__(self):
        return f'{self.user} text'
