from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('criar/', views.criar, name='criar'),
    #path('<int:id>/', views.visualizar, name='visualizar'),
    #path('<int:id>/editar/', views.editar, name='editar'),
    #path('<int:id>/excluir/', views.excluir, name='excluir'),
]
