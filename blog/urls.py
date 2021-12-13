from django.urls import path
from . import views

urlpatterns =[
    path('', views.lista_post, name = 'lista_post'),
    path('post/<int:pk>/', views.post_detalle, name='post_detalle'),
    path('post/nuevo', views.post_nuevo, name='post_nuevo'),
    path('post/<int:pk>/edit/', views.post_editar, name='post_editar'),
    path('borradores', views.post_lista_borradores, name='post_lista_borradores'),
    path('post/<pk>/publicar/', views.post_publicar, name='post_publicar'),
    path('post/<pk>/eliminar/', views.post_eliminar, name='post_eliminar'),
]
