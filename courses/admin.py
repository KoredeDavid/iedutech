from django.contrib import admin
from .models import CustomUser, Category, Course
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Course)