from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.r_create, name = 'r_create'),
    path('read/', views.r_read, name = 'r_read'),
    path('read/<int:pk>', views.r_read_one, name = 'r_read_one'),
    path('delete/<int:pk>', views.r_delete, name = 'r_delete'),
    path('update/<int:pk>', views.r_update, name = 'r_update'),
]