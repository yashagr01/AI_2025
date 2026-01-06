import tkinter as tk
import random
from tkinter import messagebox

GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

class EightPuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8 Puzzle Game")
        self.root.resizable(False, False)

        self.tiles = []
        self.buttons = []
        self.moves = 0

        self.create_widgets()
        self.shuffle_board()

    def create_widgets(self):
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack()

        for i in range(9):
            btn = tk.Button(
                frame,
                text="",
                font=("Arial", 20, "bold"),
                width=4,
                height=2,
                command=lambda i=i: self.move_tile(i)
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        self.status = tk.Label(
            self.root,
            text="Moves: 0",
            font=("Arial", 12)
        )
        self.status.pack(pady=5)

        reset_btn = tk.Button(
            self.root,
            text="New Game",
            font=("Arial", 11),
            command=self.shuffle_board
        )
        reset_btn.pack(pady=5)

    def shuffle_board(self):
        nums = list(range(9))
        while True:
            random.shuffle(nums)
            if self.is_solvable(nums) and nums != GOAL_STATE:
                break

        self.tiles = nums
        self.moves = 0
        self.update_ui()

    def update_ui(self):
        for i in range(9):
            if self.tiles[i] == 0:
                self.buttons[i].config(text="", state="disabled", bg="lightgray")
            else:
                self.buttons[i].config(
                    text=str(self.tiles[i]),
                    state="normal",
                    bg="SystemButtonFace"
                )

        self.status.config(text=f"Moves: {self.moves}")

    def move_tile(self, index):
        zero_index = self.tiles.index(0)
        if self.is_adjacent(index, zero_index):
            self.tiles[zero_index], self.tiles[index] = \
                self.tiles[index], self.tiles[zero_index]

            self.moves += 1
            self.update_ui()

            if self.tiles == GOAL_STATE:
                messagebox.showinfo(
                    "Congratulations 🎉",
                    f"You solved the puzzle in {self.moves} moves!"
                )

    def is_adjacent(self, i, j):
        row1, col1 = divmod(i, 3)
        row2, col2 = divmod(j, 3)
        return abs(row1 - row2) + abs(col1 - col2) == 1

    def is_solvable(self, board):
        inv = 0
        nums = [x for x in board if x != 0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    inv += 1
        return inv % 2 == 0


if __name__ == "__main__":
    root = tk.Tk()
    EightPuzzleGUI(root)
    root.mainloop()