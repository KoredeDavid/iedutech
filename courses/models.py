from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator, RegexValidator

username_validator = RegexValidator(regex=r'^[\w]+\Z', message=_('Enter a valid username. Your name should only '
                                                                 'letters, numbers and underscore.'), flags=0, )


class CustomUser(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=30,
        help_text=_('Letters, digits and underscore only.'),
        unique=True,
        validators=[username_validator, MinLengthValidator(5)],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), blank=False, null=True, unique=True)

    is_cleaned = False

    def clean(self):
        self.is_cleaned = True

        if self.email is not None:
            self.email = self.email.lower()

        # The reason for this custom validation is that, username field is case sensitive, which means you can have a
        # user with username 'ana' and another one with 'Ana'. The validation below handles that problem.
        if self.username is not None:
            try:
                get_username = CustomUser.objects.get(username__iexact=self.username)
                print(get_username)
            except CustomUser.DoesNotExist:
                get_username = None

            if get_username:
                if get_username.id != self.id:
                    raise ValidationError({'username': "User with this username already exists"})

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            self.full_clean()
        super().save(*args, **kwargs)


class Course(models.Model):
    name = models.CharField(max_length=100)
    video_id = models.CharField(max_length=100, default='')
    channel_id = models.CharField(max_length=100, default='')
    icon = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=255, default='')
    expectations = models.TextField(default='qwerty*qwerty')
    requirements = models.TextField(default='qwerty*qwerty')

    def __str__(self):
        return self.name


class NewsLetter(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=30)

    def clean(self):
        self.email = self.email.lower()
