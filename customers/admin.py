from django.contrib import admin

from .models import Person, Pet, Provider


class ProviderInline(admin.TabularInline):
    model =  Provider

class PetInline(admin.TabularInline):
    model = Pet

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        ProviderInline,
        PetInline,
    ]


admin.site.register(Person, PersonAdmin)

