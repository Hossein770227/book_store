from django.contrib import admin

from .models import Book, Comment

class CommentAdminInLine(admin.TabularInline):
    model = Comment
    list_display=['author', 'email', 'date_time_created']
    extra = 0



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['title', 'author', 'price', 'date_time_created', 'active']
    search_fields =['title']
    list_filter =['active']
    list_per_page = 10
    inlines =[CommentAdminInLine]


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display=['author', 'email', 'date_time_created']