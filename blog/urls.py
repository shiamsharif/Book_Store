from django.urls import path
from .views import PostListView, PostDetailView 

app_name = 'blog'

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    # path('post/<int:post_id>/comment/', CommentCreateView.as_view(), name='post_comment'),

]
