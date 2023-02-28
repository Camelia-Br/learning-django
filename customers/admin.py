from django.contrib import admin
from .models import Person, Provider, Pet


class PersonAdmin(admin.ModelAdmin):
    pass


class ProviderAdmin(admin.ModelAdmin):
    pass


class PetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Pet, PetAdmin)
