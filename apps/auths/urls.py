from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from auths.views import (
    MyObtainTokenPairView,
    UserRegisterView,
    UserMeViewSet,
)

router = DefaultRouter(trailing_slash=True)
router.register('user', UserMeViewSet, basename='user_me')

urlpatterns = [
    path('', include(router.urls)),

    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterView.as_view(), name='auth_register'),
]