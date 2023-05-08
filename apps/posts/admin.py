from django.contrib import admin
from apps.posts.models import Post
# Register your models here.

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price']