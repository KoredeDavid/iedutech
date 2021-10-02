from django.urls import path, include

from sayches import views

urlpatterns = [
    path('', views.pop, name='pop')
]
