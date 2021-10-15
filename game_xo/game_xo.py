import os

from colorama import Fore, Style

from .exceptions import custom_KeyError, custom_ValueError


class TicTacGame:
    game_board = {
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    }

    def __init__(self):
        self.first_name_gamer = ""
        self.second_name_gamer = ""

    def show_board(
        self,
    ):
        for key in self.game_board:
            if self.game_board[key] is None:
                print(key, end=" ")
            else:
                print(self.game_board[key], end=" ")
            if key % 3 == 0:
                print()

    def validate_input(self, i):
        while True:
            move = input()
            move = custom_ValueError(move)
            if move is None:
                continue
            if custom_KeyError(move, self.game_board) is False:
                continue
            if self.game_board[move] is None:
                if i % 2 == 0:
                    self.game_board[move] = "x"
                else:
                    self.game_board[move] = "o"
                break
            else:
                print(Fore.RED + "InputError", Style.RESET_ALL)

    def start_game(
        self,
    ):
        print("input name first player:", end="\t")
        self.first_name_gamer = input()
        print("input name second player:", end="\t")
        self.second_name_gamer = input()
        for i in range(9):
            os.system("clear")
            self.show_board()
            if i % 2 == 0:
                name = self.first_name_gamer
            else:
                name = self.second_name_gamer
            print(f"the player's move is {name}")
            self.validate_input(i)
            if self.check_winner():
                os.system("clear")
                print(Fore.GREEN + f"WIN {name}")
                self.show_board()
                break
        else:
            os.system("clear")
            print(Fore.RED + "draw")
            self.show_board()

    def check_winner(self):
        if (
            self.game_board[1] == self.game_board[5]
            == self.game_board[9] is not None
            or self.game_board[3] == self.game_board[5]
            == self.game_board[7] is not None
        ):
            return True
        for i in range(1, 10, 3):
            if (
                self.game_board[i] == self.game_board[i + 1]
                == self.game_board[i + 2] is not None
            ):
                return True
        for i in range(1, 4):
            if (
                self.game_board[i] == self.game_board[i + 3]
                == self.game_board[i + 6] is not None
            ):
                return True
        return False


if __name__ == "__main__":
    game = TicTacGame()

    game.start_game()
