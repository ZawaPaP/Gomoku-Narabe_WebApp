from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Player, Board
from .serializers import PlayerSerializer, BoardSerializer
from rest_framework import viewsets

def index(request):
    return HttpResponse("Hello, world. You're at the gomokunarabe index.")

def create_player(request):
    if request.method == "POST":
        name = request.POST.get("name")
        player = Player(name=name)
        player.save()
        return JsonResponse({"id": player.id, "name": player.name})
    else:
        return HttpResponse("Please use POST method")

def game_status(request, game_id):
    board = Board.objects.get(id=game_id)
    return JsonResponse({"board": board.board, "is_finished": board.is_finished})

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
