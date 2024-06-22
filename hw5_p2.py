#H24126094 統計116 李繕安
import random

# Function to create the board
def create_board(length):
    board = []
    for _ in range(length):
        if random.random() < 0.3:
            board.append('P')  # Penalty square
        else:
            board.append('_')  # Safe square
    return board

# Function to print the current board with players' positions
def print_board(board, player_a_pos, player_b_pos, player_a_penalty, player_b_penalty):
    display_board = board[:]
    if player_a_pos == player_b_pos:
        if board[player_a_pos] == 'P':
            display_board[player_a_pos] = 'x' if player_a_penalty or player_b_penalty else 'X'
        else:
            display_board[player_a_pos] = 'X'
    else:
        if board[player_a_pos] == 'P':
            display_board[player_a_pos] = 'a'
        else:
            display_board[player_a_pos] = 'A'
        
        if board[player_b_pos] == 'P':
            display_board[player_b_pos] = 'b'
        else:
            display_board[player_b_pos] = 'B'

    print(' '.join(display_board))

# Function to handle the dice roll
def roll_dice():
    return random.randint(1, 6)

# Function to move a player
def move_player(position, dice_roll, board_length):
    position += dice_roll
    if position >= board_length:
        position = board_length - 1
    return position

# Function to check if a player is on a penalty square
def is_penalty_square(board, position):
    return board[position] == 'P'

def main():
    board_length = 30
    board = create_board(board_length)
    player_a_pos = 0
    player_b_pos = 0
    player_a_penalty = False
    player_b_penalty = False
    game_over = False

    while not game_over:
        # Player A's turn
        if not player_a_penalty:
            dice_roll = roll_dice()
            player_a_pos = move_player(player_a_pos, dice_roll, board_length)
            player_a_penalty = is_penalty_square(board, player_a_pos)
        else:
            player_a_penalty = False
        
        # Player B's turn
        if not player_b_penalty:
            dice_roll = roll_dice()
            player_b_pos = move_player(player_b_pos, dice_roll, board_length)
            player_b_penalty = is_penalty_square(board, player_b_pos)
        else:
            player_b_penalty = False

        print_board(board, player_a_pos, player_b_pos, player_a_penalty, player_b_penalty)

        if player_a_pos == board_length - 1 and player_b_pos == board_length - 1:
            game_over = True
            print("Both players win!")
        elif player_a_pos == board_length - 1:
            game_over = True
            print("Player A wins!")
        elif player_b_pos == board_length - 1:
            game_over = True
            print("Player B wins!")

    # Print the board with hidden penalty squares revealed
    print("Final board with penalty squares revealed:")
    final_board = ['P' if x == 'P' else '_' for x in board]
    print(' '.join(final_board))

if __name__ == "__main__":
    main()