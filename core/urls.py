# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE
    # path('players/', include('apps.players.urls')),

    # Leave `Home.Urls` as last the last line
    path('api/v1/', include('core.api_urls')),
    path("", include("apps.home.urls")),

]
