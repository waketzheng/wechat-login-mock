from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    Oauth2AccessTokenView,
    TestView,
    UserInfoView,
)

router = DefaultRouter()
# router.register("room-users", RoomUserViewSet, basename="room-user")

urlpatterns = [
    path("oauth2/access_token/", Oauth2AccessTokenView.as_view()),
    path("userinfo/", UserInfoView.as_view()),
    path("test/", TestView.as_view()),
    path("", include(router.urls)),
]
