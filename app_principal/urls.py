from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('reguistro/', views.pagina_reguistro,name="pagina_reguistro"),
    path('reguistrar_emprendedor/', views.reguistrar_emprendedor,name='reguistrar_emprendedor'),
    path('reguistrar_producto/', views.reguistrar_producto,name='reguistrar_producto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
