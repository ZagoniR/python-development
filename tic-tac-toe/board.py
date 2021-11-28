# Tic Tac Toe board
class Board:
    # Initializes a new board.
    # A board is a dictionary in which the key is the position in the board and the value can be 'X', 'O' or ' '
    """
    Positions (moves):
    TL - top left
    TM - top middle
    TR - top right
    ML - middle left
    MM - center
    MR - middle right
    BL - bottom
    BM - bottom middle
    BR - bottom right
    """

    def __init__(self):

        self.board = {
            "TL": " ", "TM": " ", "TR": " ",
            "ML": " ", "MM": " ", "MR": " ",
            "BL": " ", "BM": " ", "BR": " "}

    # Print the board
    def print_board(self):
        print(self.board["TL"] + "|" + self.board["TM"] + "|" + self.board["TR"] + "|")
        print("-+" * 3)
        print(self.board["ML"] + "|" + self.board["MM"] + "|" + self.board["MR"] + "|")
        print("-+" * 3)
        print(self.board["BL"] + "|" + self.board["BM"] + "|" + self.board["BR"] + "|")

    # Check if the move is valid
    def is_valid_move(self, position):
        if position in self.board and self.board[position] == " ":
            return True
        else:
            return False

    # Receives a position
    # If the player is 'X' or 'O', checks if the position is valid, modifies the board and returns the modified board
    # Returns 'None' if the move is not valid
    def change_board(self, position, player_type):
        if self.is_valid_move(position):
            self.board[position] = player_type
            return self.board
        else:
            return None

    # Check if there is a winner (all possible winning combinations are checked)
    def is_winner(self, player_type):
        runs = [
            # horizontal
            ["TL", "TM", "TR"],
            ["ML", "MM", "MR"],
            ["BL", "BM", "BR"],
            # vertical
            ["TL", "ML", "BL"],
            ["TM", "MM", "BM"],
            ["TR", "MR", "BR"],
            # diagonal
            ["TL", "MM", "BR"],
            ["BL", "MM", "TR"]
        ]
        for a, b, c in runs:
            if self.board[a] == self.board[b] == self.board[c] == player_type:
                return True

        return False
