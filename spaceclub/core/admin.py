from django.contrib import admin
from .models import Contribution
from django.utils.html import format_html

# Admin Site Customization
admin.site.site_header = "Space Club Management Dashboard"
admin.site.site_title = "Space Club Admin"
admin.site.index_title = "Dashboard"

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'photo_thumbnail')
    search_fields = ('name', 'role', 'description')

    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height: 50px; border-radius: 4px;"/>', obj.photo.url)
        return "-"
    photo_thumbnail.short_description = "Photo Preview"
