from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),           # Главная страница
    path('predict/', views.predict, name='predict'),  # API endpoint
]