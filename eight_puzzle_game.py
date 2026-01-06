import random
import copy

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 represents the empty space
]

MOVES = {
    'w': (-1, 0),  # up
    's': (1, 0),   # down
    'a': (0, -1),  # left
    'd': (0, 1)    # right
}

def display_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" ".join(str(x) if x != 0 else " " for x in row))
    print()

def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def is_solved(board):
    return board == GOAL_STATE

def make_move(board, move):
    x, y = find_zero(board)
    dx, dy = MOVES[move]
    nx, ny = x + dx, y + dy

    if 0 <= nx < 3 and 0 <= ny < 3:
        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
        return True
    return False

def count_inversions(flat_board):
    inv = 0
    nums = [x for x in flat_board if x != 0]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                inv += 1
    return inv

def is_solvable(board):
    flat = sum(board, [])
    return count_inversions(flat) % 2 == 0

def generate_board():
    nums = list(range(9))
    while True:
        random.shuffle(nums)
        board = [nums[i:i+3] for i in range(0, 9, 3)]
        if is_solvable(board) and board != GOAL_STATE:
            return board

def play_game():
    board = generate_board()
    moves_count = 0

    print("8 Puzzle Game")
    print("Use W/A/S/D to move tiles. Press Q to quit.")

    while True:
        display_board(board)

        if is_solved(board):
            print(f"🎉 Congratulations! You solved it in {moves_count} moves.")
            break

        move = input("Your move (W/A/S/D): ").lower()

        if move == 'q':
            print("Game exited.")
            break

        if move in MOVES:
            if make_move(board, move):
                moves_count += 1
            else:
                print("❌ Invalid move!")
        else:
            print("❌ Invalid input!")

if __name__ == "__main__":
    play_game()