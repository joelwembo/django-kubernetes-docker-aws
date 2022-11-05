
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from apps.api_app import views
from apps.payments.views import HomePageView

from django.views import generic
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework import views, serializers, status
from rest_framework.response import Response

# class MessageSerializer(serializers.Serializer):
#     message = serializers.CharField()
# class EchoView(views.APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = MessageSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(
#             serializer.data, status=status.HTTP_201_CREATED)
        
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'api_app', views.GroupViewSet)
# router.register(r'snippets', views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('router/', include(router.urls)),
    path('snippets/', include('apps.snippets.urls')),
    path('', include('apps.flight.urls')),
    path('api/v1/flight/', include('apps.flight.urls')),
    path('payments/', include('apps.payments.urls')),
    path('stripe-store/', HomePageView.as_view(), name='home'),
    path('api-app/', include('apps.api_app.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path("", include("apps.authentication.urls")),
    # path("", include("apps.home.urls"))
]

# authentification system
#
# urlpatterns = [
#     path(r'^$', generic.RedirectView.as_view(
#          url='/api/', permanent=False)),
#     path(r'^api/$', get_schema_view()),
#     path(r'^api/auth/', include(
#         'rest_framework.urls', namespace='rest_framework')),
#     path(r'^api/auth/token/obtain/$', TokenObtainPairView.as_view()),
#     path(r'^api/auth/token/refresh/$', TokenRefreshView.as_view()),
# ]


