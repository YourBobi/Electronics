from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from companies.models import Company
from electronics_api.serializers import CompanySerializer


@api_view(["GET"])
def api_root(request, format=None):
    response = Response(
        {
            "companies": reverse("company-list", request=request, format=format),
        }
    )
    return response


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
