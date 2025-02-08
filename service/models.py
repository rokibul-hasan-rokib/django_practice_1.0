from django.db import models
from blog.models import Blog  

class Service(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="services") 
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='service_icons/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
