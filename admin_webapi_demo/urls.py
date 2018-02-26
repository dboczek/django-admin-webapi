from django.conf.urls import url
from django.conf.urls import include

from admin_webapi.routers import admin_router
from demoapp import models
from rest_framework.authtoken import views
from admin_webapi.routers import AdminRouter
from admin_webapi.permissions import IsSuperuser
# to register some other modesl, some form of autodiscovery could be added.
from demoapp import api_admin  # NOQA

admin_router.register(models.TestModel1, exclude_fields=('boolean',))

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^admin-staff/', include(admin_router.urls)),
]


# second panel
second_panel = AdminRouter(default_permission_classes=(IsSuperuser,))

second_panel.register(models.TestModel1, fields=('boolean', 'char', 'text'))
urlpatterns += [
    url(r'^admin-super/', include(second_panel.urls)),
]
