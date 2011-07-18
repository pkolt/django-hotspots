#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hotspots.conf.settings import MAP_KEY

def map_key(request):
    return {'MAP_KEY': MAP_KEY}