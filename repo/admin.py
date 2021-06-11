from django.contrib import admin
from .models import Snippet


# Register your models here.

# admin.site.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Snippet, SnippetAdmin)
