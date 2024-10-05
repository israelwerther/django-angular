# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from apps.accounts.views import (UserModelViewSet)
from apps.planets.views import PlanetModelViewSet
from apps.players.views import (PlayerModelViewSet)
from apps.resources.views import (IronMineModelViewSet, IronModelViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('users', UserModelViewSet, basename='users')
router.register('players', PlayerModelViewSet, basename='players')
router.register('planets', PlanetModelViewSet, basename='planets')

# Resources
router.register('resources/iron', IronModelViewSet, basename='resources-iron')
router.register('resources/iron-mine', IronMineModelViewSet, basename='resources-iron-mine')

app_name = 'api'

urlpatterns = [] + router.urls
