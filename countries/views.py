from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Country
import json

@csrf_exempt
def store_country(request):
    """Create a new country"""
    if request.method == 'POST':
        country = Country.store_country(request)
        return JsonResponse({'message': 'Country created successfully', 'id': country.id}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def update_country(request, country_id):
    """Update an existing country"""
    if request.method == 'POST':  # Normally, PATCH/PUT is preferred
        country = get_object_or_404(Country, id=country_id)
        country.update_country(request)
        return JsonResponse({'message': 'Country updated successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def delete_country(request, country_id):
    """Delete a country"""
    if request.method == 'DELETE':
        country = get_object_or_404(Country, id=country_id)
        country.delete_country()
        return JsonResponse({'message': 'Country deleted successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def get_country_assoc(request):
    """Retrieve all countries as an associative array (id -> name)"""
    data = Country.get_country_assoc()
    return JsonResponse({'countries': data}, status=200)


def get_country_list(request):
    """Retrieve all countries with full details"""
    countries = list(Country.objects.values())
    return JsonResponse({'countries': countries}, status=200)


def get_country_detail(request, country_id):
    """Retrieve a single country by ID"""
    country = get_object_or_404(Country, id=country_id)
    return JsonResponse({'id': country.id, 'name': country.name, 'code': country.code, 'currency': country.currency, 'status': country.status}, status=200)
