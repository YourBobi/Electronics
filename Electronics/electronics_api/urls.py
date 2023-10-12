from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"companies", views.CompanyViewSet, basename="company")
router.register(r"users", views.UserViewSet, basename="user")


urlpatterns = [
    path("", views.api_root, name="Api root"),
]

urlpatterns += router.urls
