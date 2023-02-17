from django.contrib import admin
from .models import SearchScore


class SearchScoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(SearchScore, SearchScoreAdmin)
