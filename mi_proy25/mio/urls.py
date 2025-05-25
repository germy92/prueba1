from django.urls import path
from . import views

urlpatterns = [
    path('',views.milista, name='milista'),
]
