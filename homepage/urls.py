from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('reguistrar/', views.reguistro),
    path('iniciar sesion/', views.inicio_sesion),
]