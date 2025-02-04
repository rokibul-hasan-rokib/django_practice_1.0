from django.urls import path
from .views import client_list, client_create, client_update, client_delete

urlpatterns = [
    path('', client_list, name='client_list'),
    path('create/', client_create, name='client_create'),
    path('update/<int:pk>/', client_update, name='client_update'),
    path('delete/<int:pk>/', client_delete, name='client_delete'),
]
