from django.contrib import admin
from . models import PostModel
# Register your models here.


# class PhotoInline(admin.TabularInline):
#     model = Photo


# class FileInline(admin.TabularInline):
#     model = File


# class PostAdmin(admin.ModelAdmin):
#     inlines = [PhotoInline, FileInline]


admin.site.register(PostModel)
