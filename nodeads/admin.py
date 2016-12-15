from django.contrib import admin

from .models import Culeba

class CulebaAdmin(admin.ModelAdmin):
    fields = []

admin.site.register(Culeba, CulebaAdmin)
