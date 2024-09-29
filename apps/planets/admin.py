from django.contrib import admin

from apps.resources.models import Iron, IronMine

from .models import Planet

class IronMineInline(admin.TabularInline):
    model = IronMine
    extra = 0

class IronInline(admin.TabularInline):
    model = Iron
    extra = 0

class PlanetAdmin(admin.ModelAdmin):
    inlines = [IronMineInline, IronInline]

admin.site.register(Planet, PlanetAdmin)
