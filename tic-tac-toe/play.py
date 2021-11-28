from game import Game, print_valid_entries


def play():
    game = Game()
    print_valid_entries()
    player = game.player1
    num = 9
    while num > 0:
        num -= 1
        game.printing_board()
        position = input(f"{player} add your move: ").upper()
        game.modify_board(position, player.player_type)
        if game.won_game(player.player_type):
            game.printing_board()
            print(f"{player} is the Winner! Game over!")
            break
        else:
            player = game.change_turn(player)
    if num == 0:
        print("It's a tie! Game over!")


if __name__ == "__main__":
    play()
