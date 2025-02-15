from django.contrib import admin

# Register your models here.
from .models import Brand, Category, Product, Writer

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Writer)
