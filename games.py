# Noughts and Crosses Game

# Initialise the game board
board = [' ' for _ in range(9)]

# Function to print the game board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check for a win, [bo = board and le = letter]
def win(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or
            (bo[3] == le and bo[4] == le and bo[5] == le) or
            (bo[6] == le and bo[7] == le and bo[8] == le) or
            (bo[0] == le and bo[3] == le and bo[6] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[0] == le and bo[4] == le and bo[8] == le) or
            (bo[2] == le and bo[4] == le and bo[6] == le))

# Main game loop
def play_game():
    turn = 'X'  # X starts the game
    count = 0

    for _ in range(9):  # Maximum 9 moves in a game  
        print_board()
        print(f"It's your turn, {turn}. Move to which place?")
        print("Your moves are from 0-8")
        move = int(input())

        # Check if the chosen spot is empty
        if board[move] == ' ':
            board[move] = turn

            # Check for a win
            if win(board, turn):
                print_board()
                print(f"Congratulations! Player {turn} wins!")
                break

            count += 1
            if count == 9:
                print("It's a tie!")
                break

            # Switch the player's turn
            turn = 'O' if turn == 'X' else 'X'
        else:
            print("That place is already filled. Move to which place?")

# Start the game
play_game()
