from typing import Any, List, Optional
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.http.request import HttpRequest

from .models import Person, Pet, Provider


class ProviderInline(admin.TabularInline):
    model =  Provider

    readonly_fields = (
        "sitter_score",
        "rating_score",
        "overall_rank",
    )

    def sitter_score(self, instance):
        return instance.search_score.sitter_score
    
    def rating_score(self, instance):
        return instance.search_score.rating_score
    
    def overall_rank(self, instance):
        return instance.search_score.overall_rank
    
    def has_delete_permission(self, request, obj=None):
        return False
    
class PetInline(admin.TabularInline):
    model = Pet

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        ProviderInline,
        PetInline,
    ]
    def get_inline_instances(self, request, obj):
        inline_instances = []
        ins = isinstance(Provider, ProviderInline)
        if hasattr(ins, "provider"):
            inline_instances.append(ins)

        return inline_instances
     


admin.site.register(Person, PersonAdmin)
