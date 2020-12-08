from django.contrib import admin
from .models import CustomUser, Category, Course, NewsLetter

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(NewsLetter)
