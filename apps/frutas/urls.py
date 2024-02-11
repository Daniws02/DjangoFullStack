from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='frutas'),
    path('create/', views.create, name='create'),
    path('<int:id>/', views.read, name='read'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
]
