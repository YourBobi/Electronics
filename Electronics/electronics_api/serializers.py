from django.contrib.auth.models import User
from rest_framework import serializers

from companies.models import Company
from products.models import Product

# from companies_details.models import Mail, Contacts, Address
#
#
# class MailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Mail
#         fields = ["mail"]
#
#
# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = "__all__"
#
#
# class ContactsSerializer(serializers.ModelSerializer):
#     mail = MailSerializer(source="mail_id")
#     address = AddressSerializer(source="address_id")
#
#     class Meta:
#         model = Contacts
#         fields = ["id", "mail", "address"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    companies = serializers.HyperlinkedRelatedField(
        many=True, view_name="company-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["url", "username", "email", "password", "companies"]


class CompanySerializer(serializers.ModelSerializer):
    # contacts = ContactsSerializer(source="contact_id", read_only=True)

    class Meta:
        model = Company
        fields = [
            "url",
            "level",
            "type",
            "name",
            "arrears",
            "provider_id",
            "contact_id",
            "product_id",
            "staff_id",
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["url", "name", "date", "product_model"]
