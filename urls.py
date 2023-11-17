from django.urls import path
from . import views

urlpatterns = [
    path('', views.greetings),
    path('calculation', views.calculation),
]
