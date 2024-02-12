from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='frutas'),
    path('create/', views.create, name='create_frutas'),
    path('<int:id>/', views.read, name='read_frutas'),
    path('<int:id>/update/', views.update, name='update_frutas'),
    path('<int:id>/delete/', views.delete, name='delete_frutas'),
]
