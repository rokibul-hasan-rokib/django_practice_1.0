from django.urls import path
from .views import service_list, service_form, service_delete

urlpatterns = [
    path('', service_list, name='service_list'),
    path('new/', service_form, name='service_create'),
    path('edit/<int:id>/', service_form, name='service_edit'),
    path('delete/<int:id>/', service_delete, name='service_delete'),
]
