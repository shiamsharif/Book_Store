from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from Carousel.models import Carousel
from Product.models import Brand, Category, Product
from django.db.models import Q

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.jinja"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        carousels = Carousel.objects.all().order_by('-id')[:3]
        context['carousels'] = carousels

        brands = Brand.objects.all().order_by('-id')[:8]
        context['brands'] = brands

        categories = Category.objects.all().order_by('-id')[:8]
        context['categories'] = categories
        return context

class BrandListView(ListView):
    model = Brand
    ordering = "-id"  # Orders by 'id' in descending order
    template_name = "brand_list.jinja"
    context_object_name = "brands"


class CategoryListView(ListView):
    model = Category
    ordering = "-id"  # Orders by 'id' in descending order
    template_name = "category_list.jinja"
    context_object_name = "categories"

    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

    def get(self, request, *args, **kwargs):
        # print("CALLING THE GET FUNCTION")
        category = request.GET.get('category')
        if category:
            self.object_list = Product.objects.filter(category__id=category).all()
        else:
            self.object_list = Product.objects.all()
        context = self.get_context_data(object_list=self.object_list)
        context['categories'] = Category.objects.all().order_by('-id')
        return render(request, self.template_name, context)

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.jinja'
    context_object_name = 'products'
    ordering = ['-id']


    def get_queryset(self):
        queryset = super().get_queryset()
        brands = self.request.GET.getlist('brands')
        categories = self.request.GET.getlist('categories')

        if brands:
            queryset = queryset.filter(brand__id__in=brands)

        if categories:
            queryset = queryset.filter(category__id__in=categories)
        return queryset
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all().order_by('-id')
        context['categories'] = Category.objects.all().order_by('-id')
        return context
    

    def get(self, request, *args, **kwargs):
        # print("CALLING THE GET FUNCTION")
        brand = request.GET.get('brand')
        category = request.GET.get('category')

        self.object_list = Product.objects.all()
        if brand:
            self.object_list = Product.objects.filter(brand__id=brand).all()
        # else:
        #     self.object_list = Product.objects.all()
        
        if category:
            self.object_list = Product.objects.filter(category__id=category).all()
        # else:
        #     self.object_list = Product.objects.all()


        context = self.get_context_data(object_list=self.object_list)
        context['brands'] = Brand.objects.all().order_by('-id')
        context['categories'] = Brand.objects.all().order_by('-id')
        return render(request, self.template_name, context)

    
    # def post(self, request, *args, **kwargs):
    #     brands = request.POST.getlist('brands')
    #     # categories = request.POST.getlist('categories')
    #     if brands:
    #         self.object_list = Product.objects.filter(brand__id__in=brands).all()
    #     else:
    #         self.object_list = Product.objects.all()
    #     context = self.get_context_data(object_list=self.object_list)
    #     context['brands'] = Brand.objects.all().order_by('-id')
    #     return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        brands = request.POST.getlist('brands')
        categories = request.POST.getlist('categories')
        
        # Start with an empty Q object for OR conditions
        filters = Q()

        # Add Q objects for each brand selected
        if brands:
            filters |= Q(brand__id__in=brands)
        
        # Add Q objects for each category selected
        if categories:
            filters |= Q(category__id__in=categories)
        
        # Apply the combined filter
        self.object_list = Product.objects.filter(filters).distinct()

        context = self.get_context_data(object_list=self.object_list)
        context['brands'] = Brand.objects.all().order_by('-id')
        context['categories'] = Category.objects.all().order_by('-id')
        
        return render(request, self.template_name, context)


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'product_details.jinja'
    context_object_name = 'product'






