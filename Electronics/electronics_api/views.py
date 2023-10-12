from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

from companies.models import Company
from electronics_api.serializers import CompanySerializer, UserSerializer
from .custom_filters import CompanyFilter


@api_view(["GET"])
def api_root(request, format=None):
    response = Response(
        {
            "companies": reverse("company-list", request=request, format=format),
            "users": reverse("user-list", request=request, format=format),
        }
    )
    return response


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("id")
    filter_backends = [DjangoFilterBackend]
    filterset_class = CompanyFilter


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return (
            User.objects.all().order_by("id")
            if self.request.user.is_superuser
            else User.objects.all().filter(id=self.request.user.id).order_by("id")
        )
