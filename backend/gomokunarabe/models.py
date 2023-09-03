from django.db import models
import json

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=20)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def player_turn(self):
        if self.id == 1:
            return True
        else:
            return False
    
    def player_mark(self):
        if self.id == 1:
            return "x"
        else:
            return "o"

class Board(models.Model):
    board = models.TextField()

    def __str__(self):
        return self.board
    
    def save(self, *args, **kwargs):
        if not self.board:
            self.board = json.dumps(self.create_board())
        super(Board, self).save(*args, **kwargs)

    def load_board(self):
        return json.loads(self.board)

    def add_move(self, row, column, mark):
        array_board = self.load_board()
        array_board[row][column] = mark
        self.save_board(array_board)
    
    def create_board(self):
        array_board = []
        for i in range(15):
            array_board.append([])
            for j in range(15):
                array_board[i].append(" ")
        return array_board

class Game(models.Model):
    board = models.OneToOneField(Board, on_delete=models.CASCADE, related_name='game')
    moves = models.JSONField(default=list)
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2')
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='winner', null=True)
    is_finished = models.BooleanField(default=False)

    @classmethod
    def create_new_game(cls, player1, player2):
        board = Board.objects.create()
        game = cls.objects.create(board=board, player1=player1, player2=player2)
        return game

    def __str__(self):
        return f"Game {self.id}" 

class Mark(models.Model):
    mark = models.CharField(max_length=1)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='marks')

    def __str__(self):
        return self.mark
class Cell(models.Model):
    row = models.IntegerField()
    column = models.IntegerField()
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name='cells')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='cells')

    def __str__(self):
        return self.mark

class Move(models.Model):
    row = models.IntegerField()
    column = models.IntegerField()
    mark = models.CharField(max_length=1)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_moves')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mark} at ({self.row}, {self.column}) for Game {self.game.id}"

