from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from core.views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/auth/", include("core.urls")),
    path("api/users/", include("users.urls")),
    path("api/education/", include("education.urls")),
    path("api/finance/", include("finance.urls")),
    path("api/attendance/", include("attendance.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("api/reports/", include("reports.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
