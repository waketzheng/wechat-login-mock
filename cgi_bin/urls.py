from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    GetTicketView,
    InfoView,

    TokenView,
)

router = DefaultRouter()
# router.register("room-users", RoomUserViewSet, basename="room-user")

urlpatterns = [
    path("ticket/getticket/", GetTicketView.as_view()),
    path("user/info/", InfoView.as_view()),
    path("token/", TokenView.as_view()),
    path("", include(router.urls)),
]
