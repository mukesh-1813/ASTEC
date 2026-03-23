import csv
from django.http import HttpResponse
from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from django.forms import Textarea, DateInput, TimeInput
from .models import Event, EventRegistration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location', 'event_status', 'image_thumbnail')
    search_fields = ('title', 'location')
    list_filter = ('event_status', 'date')
    
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 80})},
        models.DateField: {'widget': DateInput(attrs={'type': 'date'})},
        models.TimeField: {'widget': TimeInput(attrs={'type': 'time'})},
    }
    
    def image_thumbnail(self, obj):
        if obj.event_image:
            return format_html('<img src="{}" style="max-height: 80px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);"/>', obj.event_image.url)
        return "-"
    image_thumbnail.short_description = "Image Preview"

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'college', 'event', 'payment_status', 'transaction_id', 'registered_at')
    search_fields = ('name', 'email', 'phone', 'college', 'transaction_id')
    list_filter = ('event', 'payment_status', 'registered_at')
    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response
    export_to_csv.short_description = "Export Selected Registrations to CSV"
