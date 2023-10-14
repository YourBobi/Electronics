from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"companies", views.CompanyViewSet, basename="company")
router.register(r"products", views.ProductViewSet, basename="product")
router.register(r"users", views.UserViewSet, basename="user")


urlpatterns = [
    path("", views.api_root, name="Api root"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

urlpatterns += router.urls
