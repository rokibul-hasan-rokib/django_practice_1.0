from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from .forms import ServiceForm
from rest_framework import generics
from .serializers import ServiceSerializer

# List Services
def service_list(request):
    services = Service.objects.all()
    return render(request, 'client/pages/service/index.html', {'services': services})

# Create or Update Service
def service_form(request, id=None):
    if id:
        service = get_object_or_404(Service, id=id)
    else:
        service = None
    
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    
    return render(request, 'client/pages/service/form.html', {'form': form})

# Delete Service
def service_delete(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'client/pages/service/index.html', {'service': service})

class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
