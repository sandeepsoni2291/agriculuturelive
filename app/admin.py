from tkinter import Image
from django.contrib import admin

# Register your models here.
from .models import Seed,Product,Image

class SeedAdmin(admin.ModelAdmin):
    list_display = ['id','seed_name','seed_description','created_at','updated_at','server_ip']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','prod_name','prod_description','created_at','updated_at','prod_ip']

class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','small_img','created_at','updated_at']

admin.site.register(Seed, SeedAdmin)   
admin.site.register(Product, ProductAdmin)   
admin.site.register(Image, ImageAdmin)   