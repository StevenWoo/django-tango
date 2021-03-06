from django.contrib import admin
from rango.models import Category, Page, UserProfile

admin.site.register(Category)
#admin.site.register(Page)

class PageAdmin(admin.ModelAdmin):
    list_display = ('category','title', 'url')

admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
