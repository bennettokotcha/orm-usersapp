from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process-user', views.register_user),
]