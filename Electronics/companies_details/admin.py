from django.contrib import admin
from .models import *


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Staff._meta.fields]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Address._meta.fields]


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contacts._meta.fields]


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Mail._meta.fields]
