from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from rest_framework_jwt.views import obtain_jwt_token

from users.views import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('login/', obtain_jwt_token),
]