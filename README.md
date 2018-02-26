Installation
============
`pip install git+https://github.com/dboczek/django-admin-webapi.git#egg=django-admin-webapi`

NOTE: `pip install -e git+https://github.com/dboczek/django-admin-webapi.git#egg=django-admin-webapi` will install demoapp and sample project as well. I could separate it into separate repository but Is it important now?


```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'admin_webapi',
    ...
]

```

Simplest way to add models to api.
Add to your urls.py

```
from admin_webapi.routers import admin_router
from yourapp import models

admin_router.register(models.SomeModel1, fields=('field_name1', 'field_name2'))
admin_router.register(models.SomeModel2, fields=('field_name1', 'field_name2'))
# You can provide exclude_fields as well for more advanced examples see admin_webapi_demo/urls.py and demoapp/api_admin.py project.

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^admin-staff/', include(admin_router.urls)),
]
```

Configuration
=============
Same as Django REST framework but uses ADMIN_API dict instead of REST_FRAMEWORK dict in settings.py of your project.
All defaults are same as Django REST Framework except those changend in admin_webapi/settings.py
This way you can have separate global configuration for admin api and for other api based on DRF in your project.

By default admin_webapi limits access to the API to admin users (staff) so you need to configure some authentication method same way as it is  done in DRF.
See demoapp and admin_webapi_demo for example with Token authentication.


Check demo application
======================
You can check source on github obviously.

To check the demo application:
1. clone this repository
2. run migrations
3. run django server
4. use some client that will allow you to set request headers

Prepare some data run `./manage.py createsuperuser` twice and create two users (could be 'super' and 'staff').
Modify second user

```
./manage.py shell
from django.contrib.auth.models import User
u=User.objects.get(username='staff')
u.is_staff=False
u.save()

```

By posting username and password to
http://127.0.0.1:8000/api-token-auth/
you will obtain token you shoud send with request to API.

`Authorizaton: Token YOUR_TOKEN_HERE`

This method of authorization is not part of my library you can use any authorization that is avaliable for Django Rest Framework.


Notes
=====
Most parts of the library inherit after classes from Django REST Framework therefore you can extend them in same way as originals.
I think this make it very flexible that way.


TODO
====

* Support for some HATEOAS format (ie. JSON-LD + HYDRA)
* Suppoort for equivalent of list_fields
* Support for additional actions on collections and resources
* Better(?) support for file upload (right now it works as it works in Django Rest Framework)
* Proper HATEOAS support for relations