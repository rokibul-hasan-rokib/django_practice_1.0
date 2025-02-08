from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'client/pages/blog/index.html', {'blogs': blogs})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'client/pages/blog/form.html', {'form': form})

def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'client/pages/blog/form.html', {'form': form})