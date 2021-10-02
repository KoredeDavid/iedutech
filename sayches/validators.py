import re

import magic
from django.core.exceptions import ValidationError


# This makes sure the words are limited to 30, excluding special characters. I personally advice to use characters
# instead of this because a user can input unlimited amount of words using hyphen to space them.
def max_word(value):
    res = len(re.findall(r'\w+', value))
    if res > 30:
        raise ValidationError(f'The maximum amount of words is 30, you have {res} words')


# This checks if the file uploaded is actually an image file. If I used Django ImageField instead of FileField which
# I used, django will actually check for that but still having this validation will be an extra security.
def mime_validator(value):
    mime = magic.from_buffer(value.read(1024), mime=True)
    if 'image' not in mime:
        raise ValidationError('Please select a valid image format. It seems this image is corrupted')
    else:
        # Limits file size to 2mb
        limit = 2 * 1024 * 1024  # bytes
        if value.size > limit:
            raise ValidationError('File too large. Size should not exceed 2 MB.')
