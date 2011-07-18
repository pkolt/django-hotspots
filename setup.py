#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name            =   "django-hotspots",
    version         =   "0.2",
    author          =   "Pavel Koltyshev",
    author_email    =   "pkolt@mail.ru",
    url             =   "http://github.com/pkolt/django-hotspots/",
    description     =   "Create layers of active regions for Yandex maps. http://api.yandex.ru/maps/features/hotspots/"
)