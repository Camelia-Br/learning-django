from django.contrib import admin
from .models import Stay, Review
# Register your models here.


class StayAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Stay, StayAdmin)
admin.site.register(Review, ReviewAdmin)
