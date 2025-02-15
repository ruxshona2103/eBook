from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from social_django.urls import urlpatterns

scheme_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        description="E-book API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ruxshonaaglamkhujayeva@gmail.com"),
        license=openapi.License(name="BSD License")
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('ebook_app.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', scheme_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', scheme_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', scheme_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
