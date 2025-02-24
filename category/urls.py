from django.urls import path
from .views import category_list, category_form, category_update, category_delete,CategoryListCreateView,CategoryRetrieveUpdateDestroyView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',category_list, name='category_list'),
    path('create/', category_form, name='category_create'),
    path('update/<int:id>/', category_update, name='category_update'),
    path('delete/<int:id>/', category_delete, name='category_delete'),
    path('api/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('api/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
]
