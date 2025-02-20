from rest_framework import serializers
from .models import Blog, Category

class BlogPostSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')

    class Meta:
        model = Blog
        fields = '__all__'
