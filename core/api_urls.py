# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from apps.players.views import (PlayerModelViewSet)
from apps.resources.views import (IronModelViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('players', PlayerModelViewSet,  basename='players')
router.register('resources/iron', IronModelViewSet,  basename='resources')

app_name = 'api'

urlpatterns = [] + router.urls
