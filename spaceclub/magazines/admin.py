from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from django.forms import Textarea
from .models import Magazine

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'cover_thumbnail', 'pdf_link')
    search_fields = ('title', 'description')
    list_filter = ('publish_date',)
    
    # Improve form styling
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 80})},
    }

    def cover_thumbnail(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="max-height: 80px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);"/>', obj.cover_image.url)
        return "-"
    cover_thumbnail.short_description = "Cover Preview"

    def pdf_link(self, obj):
        if obj.pdf_file:
            return format_html('<a href="{}" target="_blank" class="button" style="padding: 5px 10px; background-color: #4a90e2; color: white; border-radius: 4px; text-decoration: none;">View PDF</a>', obj.pdf_file.url)
        return "-"
    pdf_link.short_description = "PDF Preview"
