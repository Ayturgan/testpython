from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponse

def test_view(request):
    """Simple test endpoint"""
    return HttpResponse("OK - Django is running!")

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Test Blog API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@blogapi.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', test_view, name='test'),  # Root endpoint для тестирования
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
