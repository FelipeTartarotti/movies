# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import apps
from django.contrib import admin

app = apps.get_app_config('movies')

for model_name, model in app.models.items():
    admin.site.register(model)

