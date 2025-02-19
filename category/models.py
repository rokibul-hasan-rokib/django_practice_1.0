from django.db import models

class Category(models.Model):
    STATUS_CHOICES = [
        ('1', 'Active'),
        ('2', 'Inactive'),
    ]
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name
