from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.decorators import login_required


schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version='v1',
        description="API documentation for the Task Manager project",
    ),
    public=True,
    permission_classes=[IsAdminUser],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('list_info.urls')),
    path('swagger/', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
]
