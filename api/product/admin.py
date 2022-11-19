from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','price','stock','is_active','image','category','created_at','updated_at','id']
