from django.contrib import admin
from django.urls import path, include
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('store/', include('store.urls')),
    path('tags/', include('tags.urls')),

    path('__debug__/', include(debug_toolbar.urls))
]
