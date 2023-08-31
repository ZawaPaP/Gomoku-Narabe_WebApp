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

class Board(models.Model):
    board = models.TextField()
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2')
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='winner', null=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.board
    
    def save_board(self, array_board):
        self.board = json.dumps(array_board)
        self.save()

    def load_board(self):
        return json.loads(self.board)
    

