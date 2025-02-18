from django.urls import path
from views import category_list, category_form, category_update, category_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',category_list, name="category_list")
    path('create/', category_form, name='category_create'),
    path('update/<int:id>/', category_update, name='category_update'),
    path('delete/<int:id>/', category_delete, name='category_delete'),
]
