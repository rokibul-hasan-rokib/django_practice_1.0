# from django.db import models

# class Blog(models.Model):
#     name = models.CharField(max_length=255)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     image = models.ImageField(upload_to='blog_images/')

#     def __str__(self):
#         return self.title

form django.db import models 

class Category(models.Model):
      STATUS_CHOICES = [
        ('1', 'Active'),
        ('2', 'Inactive'),
    ]
    name = models.CharField(max_length=255)
    status = models.smallIntegerField(choices = STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

