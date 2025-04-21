from django.contrib import admin
from .models import Post, Comment

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'slug', 'author', 'publish', 'status']
#     list_filter = ['status', 'created', 'publish', 'author']
#     search_fields = ['title', 'body']
#     prepopulated_fields = {'slug' : ('title',)}
#     raw_id_fields = ['author']
#     date_hierarchy = 'publish'
#     ordering = ['status', 'publish']
#     show_facets = admin.ShowFacets.ALWAYS

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'post', 'created', 'active']
#     list_filter = ['active', 'created', 'updated']
#     search_fields = ['name', 'email', 'body']


# Define inline for Comment
class CommentInline(admin.TabularInline): 
    model = Comment
    extra = 0  # No empty extra forms
    fields = ['name', 'email', 'body', 'active', 'created']
    readonly_fields = ['created']
    show_change_link = True

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS

    inlines = [CommentInline]  # Add the inline here

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']