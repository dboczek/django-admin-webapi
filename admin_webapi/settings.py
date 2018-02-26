from rest_framework.settings import APISettings
from rest_framework.settings import DEFAULTS
from rest_framework.settings import IMPORT_STRINGS
from rest_framework.settings import settings
from rest_framework.settings import setting_changed


DEFAULTS.update({
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAdminUser',
    ),
})


class AdminAPISettings(APISettings):
    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'ADMIN_API', {})
        return self._user_settings


admin_api_settings = AdminAPISettings(None, DEFAULTS, IMPORT_STRINGS)


def reload_api_settings(*args, **kwargs):
    setting = kwargs['setting']
    if setting == 'ADMIN_API':
        admin_api_settings.reload()


setting_changed.connect(reload_api_settings)
