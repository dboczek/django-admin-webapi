# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import APIRootView
from admin_webapi.settings import admin_api_settings


class AdminAPIViewMixin(object):
    renderer_classes = admin_api_settings.DEFAULT_RENDERER_CLASSES
    parser_classes = admin_api_settings.DEFAULT_PARSER_CLASSES
    authentication_classes = admin_api_settings.DEFAULT_AUTHENTICATION_CLASSES
    throttle_classes = admin_api_settings.DEFAULT_THROTTLE_CLASSES
    permission_classes = admin_api_settings.DEFAULT_PERMISSION_CLASSES
    content_negotiation_class = admin_api_settings.DEFAULT_CONTENT_NEGOTIATION_CLASS
    metadata_class = admin_api_settings.DEFAULT_METADATA_CLASS
    versioning_class = admin_api_settings.DEFAULT_VERSIONING_CLASS

    # Allow dependency injection of other settings to make testing easier.
    settings = admin_api_settings


class AdminAPIRootView(AdminAPIViewMixin, APIRootView):
    pass


class AdminAPIViewSet(AdminAPIViewMixin, ModelViewSet):
    pass
