
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.members, name='about'),
]
