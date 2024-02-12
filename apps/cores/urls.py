from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='cores'),
    path('create/', views.create, name='create_cores'),
    path('<int:id>/', views.read, name='read_cores'),
    path('<int:id>/update/', views.update, name='update_cores'),
    path('<int:id>/delete/', views.delete, name='delete_cores'),
]
