from django.urls import path
from .views import blog_list, blog_create, blog_update, blog_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('create/', blog_create, name='blog_create'),
    path('update/<int:pk>/', blog_update, name='blog_update'),
    path('delete/<int:pk>/', blog_delete, name='blog_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
