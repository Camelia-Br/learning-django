from django.contrib import admin

from .models import Person, Pet, Provider


class ProviderInline(admin.TabularInline):
    model =  Provider

    readonly_fields = (
        "sitter_score",
        "ratings_score",
        "overall_rank",
    )

class PetInline(admin.TabularInline):
    model = Pet

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        ProviderInline,
        PetInline,
    ]


admin.site.register(Person, PersonAdmin)

