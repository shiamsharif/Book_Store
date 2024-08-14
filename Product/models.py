from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='brand_photos/', null=True, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Brand(id={self.id}, name={self.name})>"


class Category(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='category_photos/', null=True, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    part_number = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return (f"<Product(id={self.id}, name={self.name}, brand={self.brand.name if self.brand else 'None'}, "
                f"category={self.category.name if self.category else 'None'}, model={self.model}, part_number={self.part_number})>")
