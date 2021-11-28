from player import Player
from board import Board


# Display possible moves in the console
def print_valid_entries():
    print("""Valid moves: 
             \rTL - top left    | TM - top middle    | TR - top right 
             \rML - middle left | MM - center        | MR - middle right
             \rBL - bottom left | BM - bottom middle | BR - bottom right""")


class Game:
    # The game defines player 1 always playing with 'X'
    def __init__(self):
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()

    def printing_board(self):
        self.board.print_board()

    def change_turn(self, player):
        if player is self.player1:
            return self.player2
        else:
            return self.player1

    def won_game(self, player):
        return self.board.is_winner(player)

    # Returns modified board if the position was valid
    # Asks the player try a different position if the position is not valid
    def modify_board(self, position, player_type):
        while self.board.change_board(position, player_type) is None:
            position = input("Position is not available/valid. Please, try again: ").upper()
        return self.board.change_board(position, player_type)
