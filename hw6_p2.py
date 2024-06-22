#H24126094 統計116 李繕安
import random

def initialize_board(height, width, num_candies):
    return [[random.randint(1, num_candies) for _ in range(width)] for _ in range(height)]

def display_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def is_valid_move(board, r1, c1, r2, c2):
    return (0 <= r1 < len(board) and 0 <= c1 < len(board[0]) and 
            0 <= r2 < len(board) and 0 <= c2 < len(board[0]) and 
            abs(r1 - r2) + abs(c1 - c2) == 1)

def switch_candies(board, r1, c1, r2, c2):
    board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]

def find_matches(board):
    matches = set()
    for r in range(len(board)):
        for c in range(len(board[0])):
            if r > 1 and board[r][c] == board[r-1][c] == board[r-2][c]:
                matches.update([(r, c), (r-1, c), (r-2, c)])
            if c > 1 and board[r][c] == board[r][c-1] == board[r][c-2]:
                matches.update([(r, c), (r, c-1), (r, c-2)])
    return matches

def crush_candies(board, matches):
    for r, c in matches:
        board[r][c] = 0

def drop_candies(board, num_candies):
    for c in range(len(board[0])):
        stack = [board[r][c] for r in range(len(board)) if board[r][c] != 0]
        stack = [0] * (len(board) - len(stack)) + stack
        for r in range(len(board)):
            board[r][c] = stack[r]
    for c in range(len(board[0])):
        for r in range(len(board)):
            if board[r][c] == 0:
                board[r][c] = random.randint(1, num_candies)

def play_game():
    height = int(input("Enter the height of the board: "))
    width = int(input("Enter the width of the board: "))
    num_candies = int(input("Enter the number of candy types: "))

    board = initialize_board(height, width, num_candies)
    score = 0
    moves = 0

    while True:
        display_board(board)
        print(f"Score: {score}")

        try:
            r1, c1, r2, c2 = map(int, input("Enter the row and column of two adjacent candies to switch (r1 c1 r2 c2): ").split())
        except ValueError:
            print("Invalid input. Please enter four integers separated by spaces.")
            continue

        if not is_valid_move(board, r1, c1, r2, c2):
            print("Invalid move. The cells must be adjacent.")
            continue

        switch_candies(board, r1, c1, r2, c2)

        while True:
            matches = find_matches(board)
            if not matches:
                break

            crush_candies(board, matches)
            score += len(matches)
            drop_candies(board, num_candies)

        moves += 1
        if moves >= 20:  # End the game after 20 moves
            print("Game over!")
            print(f"Final score: {score}")
            break

if __name__ == "__main__":
    play_game()