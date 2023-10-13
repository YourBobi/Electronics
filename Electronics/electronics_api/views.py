from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

from companies.models import Company
from products.models import Product
from electronics_api.serializers import (
    CompanySerializer,
    UserSerializer,
    ProductSerializer,
)
from .custom_filters import CompanyFilter


@api_view(["GET"])
def api_root(request, format=None):
    response = Response(
        {
            "companies": reverse("company-list", request=request, format=format),
            "products": reverse("product-list", request=request, format=format),
        }
    )
    if request.user.is_superuser:
        response.data["users"] = reverse("user-list", request=request, format=format)
    return response


@permission_classes([permissions.IsAuthenticated])
class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CompanyFilter

    def get_queryset(self):
        return (
            Company.objects.all().order_by("id")
            if self.request.user.is_superuser
            else Company.objects.all().filter(owner=self.request.user).order_by("id")
        )


@permission_classes([permissions.IsAuthenticated])
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("id")
    http_method_names = ["get", "post", "head"]


@permission_classes([permissions.IsAdminUser])
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return (
            User.objects.all().order_by("id")
            if self.request.user.is_superuser
            else User.objects.all().filter(id=self.request.user.id).order_by("id")
        )
