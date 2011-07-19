#!/usr/bin/env python
# -*- coding: utf-8 -*-

from optparse import make_option
from django.core.management.base import BaseCommand
from django.core.exceptions import ImproperlyConfigured
from hotspots import HotspotsManager

class HotspotsBaseCommand(BaseCommand):
    help = 'Generate tiles from map'
    scale = None
    hotspots_class = HotspotsManager
    option_list = BaseCommand.option_list + (
        make_option('--no_remove',
            default=False,
            action='store_true',
            help='Do not remove the old tiles to create new'),
        )
    
    def get_iterable(self):
        raise NotImplemented

    def handle(self, *args, **options):
        if self.scale is None:
            raise ImproperlyConfigured('Value scale must be a number or a tuple')
        verbosity = int(options.get('verbosity'))
        hotspots_manager = self.hotspots_class()
        iterable = self.get_iterable()
        no_remove = options.get('no_remove')
        hotspots_manager.generate_tiles(iterable, self.scale, verbosity=verbosity, no_remove=no_remove)
