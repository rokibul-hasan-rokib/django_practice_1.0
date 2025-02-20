from django.urls import path
from .views import client_list, client_create, client_update, client_delete,ClientListCreateView,ClientRetrieveUpdateDestroyView

urlpatterns = [
    path('', client_list, name='client_list'),
    path('create/', client_create, name='client_create'),
    path('update/<int:pk>/', client_update, name='client_update'),
    path('delete/<int:pk>/', client_delete, name='client_delete'),
    path('api/', ClientListCreateView.as_view(), name='client-list-create'),
    path('api/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),
]
