from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Comment
from .forms import CommentForm

class PostListView(ListView):
    model = Post
    template_name = "../Templates/blog/list.html"
    context_object_name = "posts"
    paginate_by = 5
    

class PostDetailView(DetailView, CreateView):
    model = Post
    # queryset = Post.publisheda.all()
    form_class = CommentForm
    template_name = "../Templates/blog/detail.html"
    context_object_name = "post"
    #success_url = reverse_lazy("post_detail" pk=self.pk)
    
    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs['pk'])
        form.instance.post = post
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all().order_by('-created')
        return context
    
    def get_success_url(self):
        # Redirect to the same post detail page using the pk from the URL
        return reverse('blog:post_detail', kwargs={'pk': self.kwargs['pk']})


    
    
# class CommentCreateView(CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'comment_form.html'

#     def form_valid(self, form):
#         post = Post.objects.get(pk=self.kwargs['pk'])
#         form.instance.post = post
#         return super().form_valid(form)

#     def get_success_url(self):
#         return self.object.post.get_absolute_url()