from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("electronics_api/", include("electronics_api.urls")),
]
