from django.contrib import admin
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin

from .models import Post, Images

# Register your models here.

@admin.register(Post)
class PostModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['title', 'updated_at', 'created_at']
    search_fields = ['title', 'desc', 'slug',]
    ordering = ('updated_at',)
    
    prepopulated_fields = {'slug' : ('title',)}


@admin.register(Images)
class ImagesModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]
    list_filter = ['post',]
    ordering = ('-created_at',)