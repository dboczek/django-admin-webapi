from admin_webapi.views import AdminAPIViewSet
from django.contrib.auth import get_user_model
from admin_webapi.serializers import AdminModelSerializer
from admin_webapi.routers import admin_router

User = get_user_model()


class UserSerializerForSuperuser(AdminModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializerForStaff(AdminModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff')
        read_only_fields = ('username', 'email, is_staff')


class UserAdminApiViewSet(AdminAPIViewSet):
    def get_queryset(self):
        # custom queryset, based on currently authenticated user
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(is_superuser=False)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return UserSerializerForSuperuser
        return UserSerializerForStaff

admin_router.register(UserAdminApiViewSet, prefix=u"auth-user", base_name=u'user')
