"""
URL configuration for movie_rental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from decouple import config
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static


schema_view = get_schema_view(
        openapi.Info(
            title="Movies Rental API",
            default_version='v1',
            description="Documentation of Project",
            contact=openapi.Contact(email=""),
            public=True
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )



urlpatterns = [
    path('api/',include('movies.urls')),
    path('api/',include('users.urls'))
]

if config('ENVIRONMENT') == 'local':
    urlpatterns += [path('admin/', admin.site.urls)]
else:
    urlpatterns += [path(config('ADMIN_URL','admin/'), admin.site.urls)]


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
        path('__debug__/', include('debug_toolbar.urls')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)