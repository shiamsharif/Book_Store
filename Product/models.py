from django.db import models

from django.utils.text import slugify

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
    

class Writer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='writer_photos/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    # To add and save slug id
    def save(self, *args, **kwargs):
        if not self.slug:  # Auto-generate slug if empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Writer(id={self.id}, name={self.name})>"


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    writers = models.ManyToManyField(Writer)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return (f"<Product(id={self.id}, name={self.name}, brand={self.brand.name if self.brand else 'None'}, "
                f"category={self.category.name if self.category else 'None'}, model={self.model}, part_number={self.part_number})>")
