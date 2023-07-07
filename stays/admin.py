from django.contrib import admin

from .models import Review, Stay

# Register your models here.


class StayAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Stay, StayAdmin)
admin.site.register(Review, ReviewAdmin)
