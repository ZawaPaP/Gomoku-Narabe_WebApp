from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Player, Game, Board
from .serializers import PlayerSerializer, GameSerializer, BoardSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return HttpResponse("Hello, world. You're at the gomokunarabe index.")

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def create(self, request, *args, **kwargs):
        board = Board.objects.create()
        serializer = BoardSerializer(board)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AddMoveView(APIView):
    def post(request, game_id):
        if request.method == "POST":
            try:
                board = Game.objects.get(id=game_id).load_board()
            except Board.DoesNotExist:
                return HttpResponse("Board does not exist")
            row = request.POST.get("row")
            column = request.POST.get("column")
            mark = request.POST.get("mark")
            board.add_move(row, column, mark)
            return Response({"board": board.board}, status=status.HTTP_200_OK)
        else:
            return HttpResponse("Please use POST method")
