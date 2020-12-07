from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator


@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r'^[\w]+\Z'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and underscore.'
    )
    flags = 0


username_validator = UnicodeUsernameValidator()


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

    def clean(self):
        self.username = self.username.capitalize()
        self.email = self.email.lower()
        self.display_name = self.username


class Category(models.Model):
    name = models.CharField(max_length=100, )
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, )
    about = models.TextField()

    # enrolled = models.BooleanField(default=False)

    def __str__(self):
        return self.name + f' | {self.category} category'





class NewsLetter(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=30)

    def clean(self):
        self.email = self.email.lower()


