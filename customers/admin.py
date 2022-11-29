from django.contrib import admin
from .models import Person, Provider, Pet
# Register your models here.


class CustomersAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, CustomersAdmin)
admin.site.register(Provider, CustomersAdmin)
admin.site.register(Pet, CustomersAdmin)
