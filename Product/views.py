from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from Carousel.models import Carousel
from Product.models import Brand, Category, Product, Writer, Contact
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .forms import ContactForm, ProductForm
from .utils import Send_mail
from cart.forms import CartAddProductForm
from django.views.generic.edit import CreateView

# Create your views here.
class HomePageView(FormView):
    template_name = "home.html"
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        Send_mail(self, form)  #utils
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        carousels = Carousel.objects.all().order_by('-id')[:3]
        context['carousels'] = carousels

        brands = Brand.objects.all().order_by('-id')[:8]
        context['brands'] = brands

        categories = Category.objects.all().order_by('-id')[:8]
        context['categories'] = categories

        products = Product.objects.all().order_by('-id')[:20]
        context['products'] = products
        
        # Adding the cart product form
        context['cart_product_form'] = CartAddProductForm()

        return context

class BrandListView(ListView):
    model = Brand
    ordering = "-id"  # Orders by 'id' in descending order
    template_name = "brand_list.html"
    context_object_name = "brands"
    paginate_by = 12


class CategoryListView(ListView):
    model = Category
    ordering = "-id"  # Orders by 'id' in descending order
    template_name = "category_list.html"
    context_object_name = "categories"
    paginate_by = 12

    
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
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['-id']
    paginate_by = 18


    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Retrieve filter values from GET request
        brands = self.request.GET.getlist('brand')  # Using name="brand[]"
        categories = self.request.GET.getlist('category')  # Using name="category[]"

        # Create a Q object for filtering
        filters = Q()

        # Apply brand filters if selected
        if brands:
            filters &= Q(brand__id__in=brands)

        # Apply category filters if selected
        if categories:
            filters &= Q(category__id__in=categories)

        # Return the filtered queryset
        return queryset.filter(filters).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all().order_by('-id')  # Pass all brands to template
        context['categories'] = Category.objects.all().order_by('-id')  # Pass all categories to template
        return context


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['cart_product_form'] = CartAddProductForm()
        return context


class WriterDetailView(DetailView):
    model = Writer
    template_name = "writer_detail.html"
    context_object_name = "writer"

    def get_object(self):
        return get_object_or_404(Writer, slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(writers=self.object)
        return context


# search:
class Search(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query', '').strip()
        if query:
            return Product.objects.filter(
                Q(name__icontains=query) | 
                Q(writers__name__icontains=query)  # ManyToManyField lookup
            ).distinct().prefetch_related('writers')  # Optimized query , distinct use to remove duplicate
        return Product.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '').strip()
        return context


class ContactView(FormView):
    template_name = "../Templates/contactus.html"
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        Send_mail(self, form)
        return super().form_valid(form)
    
class PrivacyPolicyView(TemplateView):
    template_name = "../Templates/privacypolicy.html"

class AboutView(TemplateView):
    template_name = "../Templates/about.html"

class TarmsandconditionsView(TemplateView):
    template_name = "../Templates/terms&conditions.html"
    
# CURD

class ProductCreateView(CreateView):
    model = Product
    # form_class = ProductForm
    fields = ['name', 'brand', 'category', 'price', 'image', 'description', 'writers']
    template_name = 'create.html'
    success_url = reverse_lazy('home')
