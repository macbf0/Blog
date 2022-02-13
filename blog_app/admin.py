from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','label','author','text','publish','status')
    list_filter = ('author','status','publish','date_created')
    search_fields = ('title','text')
    date_hierarchy = 'publish'
    prepopulated_fields = {'label':('title',)}
    raw_id_fields = ('author',)
    ordering = ('status','publish')
