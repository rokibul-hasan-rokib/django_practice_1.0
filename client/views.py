from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm

# List all clients
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client/pages/client/index.html', {'clients': clients})

# Create a new client
def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client/pages/client/forms.html', {'form': form})

# Update an existing client
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/pages/client/forms.html', {'form': form})

# Delete a client
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect('client_list')
    return render(request, 'client/pages/client/delete.html', {'client': client})
