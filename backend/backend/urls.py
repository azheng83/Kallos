
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("custom_user.urls")),
    path("products/", include("products.urls")),
    path("admin/", admin.site.urls),
]
