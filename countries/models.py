from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    status = models.IntegerField()

    @classmethod
    def prepare_data(cls, request):
        """Extract and return required data from the request"""
        return {
            'name': request.POST.get('name'),
            'code': request.POST.get('code'),
            'currency': request.POST.get('currency'),
            'status': request.POST.get('status'),
        }

    @classmethod
    def store_country(cls, request):
        """Create a new country record"""
        data = cls.prepare_data(request)
        return cls.objects.create(**data)

    def update_country(self, request):
        """Update an existing country record"""
        data = self.prepare_data(request)
        for key, value in data.items():
            setattr(self, key, value)
        self.save()
        return self

    def delete_country(self):
        """Delete the country record"""
        self.delete()

    @classmethod
    def get_country_assoc(cls):
        """Get all countries as a dictionary (id -> name)"""
        return dict(cls.objects.values_list('id', 'name'))

    def __str__(self):
        return self.name
