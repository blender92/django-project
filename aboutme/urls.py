from . import views
from django.urls import path

urlpatterns = [
    path('', views.aboutme, name='aboutme.html'),
]
 