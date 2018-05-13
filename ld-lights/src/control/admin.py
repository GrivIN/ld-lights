from django.contrib import admin

from .models import Light


class LightAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'port',
        'red',
        'green',
        'blue',
        'is_on',
    )
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Light, LightAdmin)
