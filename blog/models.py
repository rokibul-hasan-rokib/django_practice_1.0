from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title
