from django.contrib.auth.models import User
from rest_framework import serializers

from companies.models import Company
from products.models import Product

from companies_details.models import Mail, Contacts, Address


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ["mail"]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["country_code", "country", "city", "street", "house_number"]


class ContactsSerializer(serializers.ModelSerializer):
    mail = MailSerializer(source="mail_id")
    address = AddressSerializer(source="address_id")

    class Meta:
        model = Contacts
        fields = ["mail", "address"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    companies = serializers.HyperlinkedRelatedField(
        many=True, view_name="company-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["url", "username", "email", "password", "companies"]


class CompanySerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(source="contact_id", read_only=True)
    arrears_usd = serializers.ReadOnlyField(source="arrears.amount")

    def create(self, validated_data):
        validated_data = {k: v for k, v in validated_data.items() if v}
        company = Company.objects.create(**validated_data)
        company.save_user(self.context["request"].user)
        return company

    class Meta:
        model = Company
        fields = [
            "url",
            "level",
            "type",
            "name",
            "arrears_usd",
            "provider_id",
            "contact_id",
            "product_id",
            "staff_id",
            "contacts",
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["url", "name", "date", "product_model"]
