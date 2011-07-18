#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings

MAP_KEY = getattr(settings, 'HOTSPOTS_MAP_KEY', '')