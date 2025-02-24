from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm
from rest_framework import generics
from .serializers import CategorySerializer


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'client/pages/category/index.html', {'categories': categories})


def category_form(request, id=None):
    if id:
        category = get_object_or_404(Category, id=id)
    else:
        category = None
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'client/pages/category/form.html', {'form': form})

def category_update(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'client/pages/category/form.html', {'form': form})

def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'client/pages/category/delete.html', {'category': category})

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Retrieve, Update, Delete API
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
