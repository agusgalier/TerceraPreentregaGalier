from django.urls import path
from inicio import views

app_name='inicio'

urlpatterns = [
    
    path('',views.inicio, name='inicio'),
    path('futbolistas/crear/',views.crear_futbolista,name='crear_futbolista'),
    path('futbolistas',views.lista_futbolistas,name='lista_futbolistas'),
    path('basquetbolistas/crear/',views.crear_basquetbolista,name='crear_basquetbolista'),
    path('basquetbolistas',views.lista_basquetbolistas,name='lista_basquetbolistas'),
    path('tenista/crear/',views.crear_tenista,name='crear_tenista'),
    path('tenista',views.lista_tenistas,name='lista_tenistas'),
 ]
