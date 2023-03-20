from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import PostViewSet


router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),
]
