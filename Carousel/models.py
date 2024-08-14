from django.db import models

# Create your models here.

class Carousel(models.Model):
    photo = models.ImageField(upload_to='carousel_photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Carousel {self.id}"

    def __repr__(self):
        return f"<Carousel(id={self.id}, created_at={self.created_at}, updated_at={self.updated_at})>"
    
# def save(self, *args, **kwargs):
#     super().save(*args, **kwargs)
#     # Cleanup after saving the new image
#     carousels = Carousel.objects.order_by('-created_at')
#     if carousels.count() > 3:
#         old_carousels = carousels[3:]  # Exclude the latest 3 images
#         old_carousels.delete()