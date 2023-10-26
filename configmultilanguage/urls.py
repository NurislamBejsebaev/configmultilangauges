from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('readers/', include('reader.urls')),
    path('users/', include('usersapp.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api_schema/', get_schema_view(title='API Schema', description='test'), name='api_schema'),
    path('docs/', TemplateView.as_view(
         template_name='docs.html',
         extra_context={'schema_url': 'api_schema'}
         ),
         name='swagger-ui'),
    path('i18n/', include('django.conf.urls.i18n')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    path('books/', include('core.urls')),
)
