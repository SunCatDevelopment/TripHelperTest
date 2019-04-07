from django.urls import path
from . import views

urlpatterns = [
    path('', views.place, name='place'),
    path('place/<int:pk>/', views.detail, name='detail'),
]