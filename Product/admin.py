from django.contrib import admin

# Register your models here.
from .models import Brand, Category, Product, Writer, Contact

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Writer)
admin.site.register(Contact)
