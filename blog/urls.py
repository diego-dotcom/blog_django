from django.urls import path
from . import views

urlpatterns =[
    path('', views.lista_post, name = 'lista_post'),
]
