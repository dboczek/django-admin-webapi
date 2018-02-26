from rest_framework.routers import DefaultRouter
from admin_webapi.settings import admin_api_settings
from admin_webapi.views import AdminAPIRootView
from admin_webapi.views import AdminAPIViewSet
from django.db.models.base import ModelBase
from admin_webapi.serializers import AdminModelSerializer


class AdminRouter(DefaultRouter):
    APIRootView = AdminAPIRootView
    root_view_name = 'admin-api-root'
    default_permission_classes = None

    def __init__(self, *args, **kwargs):
        if 'root_renderers' in kwargs:
            self.root_renderers = kwargs.pop('root_renderers')
        else:
            self.root_renderers = list(admin_api_settings.DEFAULT_RENDERER_CLASSES)
        if 'default_permission_classes' in kwargs:
            self.default_permission_classes = kwargs.pop('default_permission_classes')
        super(DefaultRouter, self).__init__(*args, **kwargs)

    def register(self, viewset_or_model, prefix=None, base_name=None, fields=None, exclude_fields=None):
        if isinstance(viewset_or_model, ModelBase):
            Model = viewset_or_model
            if not prefix:
                prefix = '-'.join((Model._meta.app_label, Model._meta.model_name))
            if not (fields or exclude_fields):
                include_fields = '__all__'
            else:
                include_fields = fields

            class Serializer(AdminModelSerializer):
                class Meta:
                    model = Model
                    fields = include_fields
                    exclude = exclude_fields

            class ViewSet(AdminAPIViewSet):
                if self.default_permission_classes:
                    permission_classes = self.default_permission_classes
                queryset = Model.objects.all()
                serializer_class = Serializer
            viewset = ViewSet
        else:
            if not prefix:
                raise Exception('When registering viewset prefix is mandatory')
            if fields or exclude_fields:
                raise Exception('When registering viewset fields and exclude_fields are not supported')
            viewset = viewset_or_model
        super(AdminRouter, self).register(prefix, viewset, base_name)


admin_router = AdminRouter()
