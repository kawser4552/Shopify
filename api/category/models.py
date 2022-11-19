from django.db import models
from rest_framework import serializers

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'