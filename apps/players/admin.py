from django.contrib import admin

from apps.planets.models import Planet

from .models import Player


class PlanetInline(admin.TabularInline):
    model = Planet
    extra = 1

class PlayerAdmin(admin.ModelAdmin):
    inlines = [PlanetInline]

admin.site.register(Player, PlayerAdmin)
