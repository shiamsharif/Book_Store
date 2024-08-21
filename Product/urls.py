from django.urls import path
from .views import HomePageView, BrandListView, CategoryListView, ProductListView, ProductDetailsView, Search
from django.conf.urls.static import static
from Main import settings

# from django.http import HttpResponse
# from django.views import View


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("brand-list/", BrandListView.as_view(), name="brand_list"),
    path("category-list/", CategoryListView.as_view(), name="category_list"),
    path("product-list/", ProductListView.as_view(), name="product_list"),
    path("product-list/<int:id>/", ProductListView.as_view(), name="product_detail"),
    path("product/<int:pk>/", ProductDetailsView.as_view(), name='product_details'),
    path("search/", Search, name='search'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)