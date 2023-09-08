from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
   # list_display = ('name', 'body', 'created_on')
   # search_fields = ('name', 'email', 'body')
   # actions = ['approved_comments']
    # list_filter = ('approved', 'created_on')
# admin.site.register(Post)

# def approve_comments(self, request, queryset):
    # queryset.update(approved=True)
# Register your models here.
