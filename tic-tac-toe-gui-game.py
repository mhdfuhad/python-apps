from tkinter import *


class TicTacToeGame:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe Game")
        master.geometry("380x530")

        self.buttonsList = []
        self.count = 9  # No. of turns
        # Array Board initialization
        self.xoBoard = [[0] * 3 for _ in range(3)]

        self.resultLabel = Label(
            master, text="Player 1 is O, Player 2 is X", width=30, justify="center", padx=10, pady=10, font=("Arial", 12))
        self.resultLabel.grid(row=4, column=0, columnspan=3)

        restartBtn = Button(master, text="Restart", pady=5, padx=10,
                            command=self.restart_game, font=("Arial", 12))
        restartBtn.grid(row=5, column=1)

        for i in range(9):
            row, col = divmod(i + 3, 3)
            btn = Button(master, text=" ", pady=40, padx=40,
                         command=lambda num=i: self.add_xo(num), width=2, font=("Arial", 25))
            btn.grid(row=row, column=col)
            self.buttonsList.append(btn)

    def add_xo(self, idx):
        if self.count != 0:
            row, col = divmod(idx, 3)

            player_symbol = "X" if self.count % 2 == 0 else "O"
            self.xoBoard[row][col] = player_symbol  # Update Array Board
            self.buttonsList[idx].config(text=player_symbol, state=DISABLED)
            self.count -= 1

            if self.check_winner():
                for btn in self.buttonsList:
                    btn.config(state=DISABLED)

                self.resultLabel.config(
                    text=f"Player {'1' if player_symbol == 'O' else '2'} Wins!")

            elif self.count == 0:
                self.resultLabel.config(text=f"It's a tie!")

    def check_winner(self):
        def check_line(line):
            return line[0] == line[1] == line[2] and isinstance(line[0], str)

        # Check rows and columns
        for i in range(3):
            if check_line(self.xoBoard[i]) or check_line([self.xoBoard[j][i] for j in range(3)]):
                return True

        # Check diagonals
        if check_line([self.xoBoard[i][i] for i in range(3)]) or check_line(
                [self.xoBoard[i][2 - i] for i in range(3)]):
            return True

        return False

    def restart_game(self):
        self.count = 9
        self.resultLabel.config(text="Player 1 is O, Player 2 is X")

        for i in range(9):
            row, col = divmod(i, 3)
            self.buttonsList[i].config(text=" ", state=ACTIVE)
            self.xoBoard[row][col] = 0


if __name__ == "__main__":
    root = Tk()
    game = TicTacToeGame(root)
    root.minsize(380, 530)
    root.maxsize(380, 530)
    root.mainloop()
