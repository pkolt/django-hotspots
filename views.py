#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured
from django.views.generic import TemplateView

class HotspotsView(TemplateView):
    template_name = 'hotspots/yandex-maps.html'
    hotspots_manager_class = None

    def get_context_data(self, **kwargs):
        if self.hotspots_manager_class is None:
            raise ImproperlyConfigured("Set the value of `hotspots_manager_class`")
        context = self.hotspots_manager_class().get_view_context()
        return context