from django.contrib import admin
from .models import About, Home, Project, Blog, Service, Contactme, Sponsor
from comment.models import Comment


# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_update', 'create_at']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'phone', 'last_update', 'create_at']


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'last_update', 'create_at']
    search_fields = ['title']
    list_filter = ['create_at']
    inlines = [CommentInLine]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['icon', 'title', 'created_at']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['text', 'last_update']
    search_fields = ['text']
    list_filter = ['text']


admin.site.register(Home, HomeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Sponsor)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Contactme)

# admin.site.register(Resume)
