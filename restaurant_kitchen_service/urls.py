from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("restaurant.urls", namespace="restaurant")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "restaurant.views.page_not_found"
handler403 = "restaurant.views.forbidden"
