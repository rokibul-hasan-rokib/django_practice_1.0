from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'client/pages/category/index.html', {'categories': categories})