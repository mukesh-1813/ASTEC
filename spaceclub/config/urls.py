import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

admin.site.site_header = "ASTEC Space Club Admin"
admin.site.site_title = "ASTEC Space Club Admin Portal"
admin.site.index_title = "Welcome to ASTEC Space Club Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('magazines/', include('magazines.urls')),
    path('events/', include('events.urls')),
]

# Force serving media files in production (Render)
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
