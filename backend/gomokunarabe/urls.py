from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"players", views.PlayerViewSet)
router.register(r"boards", views.BoardViewSet)


urlpatterns = [
    path("", views.index, name = "index"), 
    path("api/", include(router.urls)),
    path("create_player", views.create_player, name = "create_player"),
    path("game_status/<int:game_id>", views.game_status, name = "game_status"),
]
