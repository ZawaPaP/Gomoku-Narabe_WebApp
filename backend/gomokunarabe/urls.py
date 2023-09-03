from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"players", views.PlayerViewSet)
router.register(r"game", views.GameViewSet)
router.register(r"board", views.BoardViewSet)


urlpatterns = [
    path("", views.index, name = "index"), 
    path("api/", include(router.urls)),
    path("add_move/<int:game_id>", views.AddMoveView.as_view(), name = "add_move"),
]
