from django.contrib import admin
from .models import CustomUser, Course, NewsLetter

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(NewsLetter)
