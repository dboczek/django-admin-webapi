# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import OrderedDict
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_framework.routers import APIRootView
from rest_framework.routers import reverse
from rest_framework.routers import NoReverseMatch

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
    api_root_dict = None

    def get(self, request, *args, **kwargs):
        # Return a plain {"name": "hyperlink"} response.
        ret = OrderedDict()
        namespace = request.resolver_match.namespace
        for key, url_name in self.api_root_dict.items():
            if namespace:
                url_name = namespace + ':' + url_name
            try:
                ret[key] = reverse(
                    url_name,
                    args=args,
                    kwargs=kwargs,
                    request=request,
                    format=kwargs.get('format', None)
                )
            except NoReverseMatch:
                # Don't bail out if eg. no list routes exist, only detail routes.
                continue

        return Response(ret)


class AdminAPIViewSet(AdminAPIViewMixin, ModelViewSet):
    pass
