
from django.contrib import admin
from .models import MenuItem,Feedback

admin.site.register(Feedback)
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
