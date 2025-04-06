from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store_country, name='store_country'),
    path('update/<int:country_id>/', views.update_country, name='update_country'),
    path('delete/<int:country_id>/', views.delete_country, name='delete_country'),
    path('list/', views.get_country_list, name='get_country_list'),
    path('detail/<int:country_id>/', views.get_country_detail, name='get_country_detail'),
    path('assoc/', views.get_country_assoc, name='get_country_assoc'),
]
