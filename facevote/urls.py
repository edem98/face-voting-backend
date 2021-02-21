from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', admin.site.urls),
    path('api/election/', include('canditate.api.urls')),
    path('api/elector/', include('elector.api.urls')),
    path('api/survey/', include('survey.api.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
