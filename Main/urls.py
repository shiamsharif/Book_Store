
from django.contrib import admin
from django.urls import path, include

# Add this it change the header of the admin panel. 
admin.site.site_header = 'Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path("accounts/", include("django.contrib.auth.urls")),
    # path("accounts/", include("accounts.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('Product.urls')),

    

]
