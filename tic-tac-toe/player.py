# Initialize a player with type 'X' or 'O'
class Player:
    def __init__(self, player_type):
        self.player_type = player_type

    def __str__(self):
        return f"Player {self.player_type}"
