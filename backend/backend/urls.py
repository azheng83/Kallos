from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("custom_user.urls")),
    path("", include("products.urls")),
    path("", include("store.urls")),
    path("admin/", admin.site.urls),
]
