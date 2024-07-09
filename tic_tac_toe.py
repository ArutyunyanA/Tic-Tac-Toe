class TicTacToe:
    def __init__(self, player1="X", player2="O"):
        self.board = list(range(1, 10))
        self.current_player = player1
        self.players = {player1: player2, player2: player1}
        self.winner = None

    def draw_board(self):
        print("-" * 13)
        for i in range(3):
            print("|", self.board[0 + i * 3], "|", self.board[1 + i * 3], "|", self.board[2 + i * 3], "|")
            print("-" * 13)

    def take_input(self):
        valid = False
        while not valid:
            player_answer = input(f"Куда поставим {self.current_player}? ")
            try:
                player_answer = int(player_answer)
                if 1 <= player_answer <= 9:
                    if str(self.board[player_answer - 1]) not in "XO":
                        self.board[player_answer - 1] = self.current_player
                        valid = True
                    else:
                        print("Эта клетка уже занята!")
                else:
                    print("Некорректный ввод. Введите число от 1 до 9.")
            except ValueError:
                print("Некорректный ввод. Вы уверены, что ввели число?")

    def check_win(self):
        # Выигрышные комбинации: горизонтали, вертикали, диагонали
        win_coords = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтальные
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикальные
            (0, 4, 8), (2, 4, 6)  # Диагональные
        )
        for each in win_coords:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                self.winner = self.board[each[0]]
                return True
        return False

    def switch_player(self):
        self.current_player = self.players[self.current_player]

    def play(self):
        counter = 0
        while not self.winner and counter < 9:
            self.draw_board()
            self.take_input()
            counter += 1
            if counter >= 5 and self.check_win():
                self.draw_board()
                print(f"{self.winner} выиграл!")
                return
            self.switch_player()
        self.draw_board()
        if not self.winner:
            print("Ничья!")

if __name__ == "__main__":
    print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
    game = TicTacToe()
    game.play()
    input("Нажмите Enter для выхода!")
