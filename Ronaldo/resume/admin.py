from django.contrib import admin
from .models import Education, Experience, Awards, Skill_one, Skill_two


# Register your models here.

class Skill_oneAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


class Skill_twoAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill_one, Skill_oneAdmin)
admin.site.register(Skill_two, Skill_twoAdmin)
admin.site.register(Awards)
