from django.urls import path
from .views import HomePageView, BrandListView, CategoryListView, ProductListView, ProductDetailsView, Search, WriterDetailView, ContactView, PrivacyPolicyView, AboutView, TarmsandconditionsView, ProductCreateView
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

    path("writer/<slug:slug>/", WriterDetailView.as_view(), name="writer_detail"),

    path("search/", Search.as_view(), name='search'),

    path('contact/', ContactView.as_view(), name='contact'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacypolicy'),
    path('about/', AboutView.as_view(), name='about'),
    path('tarms-and-conditions/', TarmsandconditionsView.as_view(), name='tarmsandconditions'),
    
    #CURD
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)