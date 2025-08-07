# Created by: Karishma Rajput 👩‍💻

import math

# Initialize the 3x3 board
board = [' ' for _ in range(9)]

def show_board():
    print("\n")
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        print(" " + row)
        if i < 2:
            print("---|---|---")
    print("\n")

def check_winner(b, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for pattern in win_patterns:
        if all(b[i] == player for i in pattern):
            return True
    return False

def is_draw(b):
    return ' ' not in b

def get_available_moves(b):
    return [i for i in range(9) if b[i] == ' ']

def minimax(b, depth, is_maximizing):
    if check_winner(b, 'O'):
        return 10 - depth
    elif check_winner(b, 'X'):
        return depth - 10
    elif is_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(b):
            b[move] = 'O'
            score = minimax(b, depth + 1, False)
            b[move] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(b):
            b[move] = 'X'
            score = minimax(b, depth + 1, True)
            b[move] = ' '
            best_score = min(best_score, score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = 'O'

def play_game():
    print("Welcome to Tic-Tac-Toe! 🧠 (You: X | AI: O)")
    show_board()

    while True:
        # Player move
        try:
            player_move = int(input("Choose your move (1-9): ")) - 1
            if board[player_move] != ' ':
                print("Oops! That spot is taken. Try again.")
                continue
        except (IndexError, ValueError):
            print("Invalid input. Enter a number from 1 to 9.")
            continue

        board[player_move] = 'X'
        show_board()

        if check_winner(board, 'X'):
            print("🎉 You win! Amazing job.")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

        # AI move
        print("AI is thinking...\n")
        ai_move()
        show_board()

        if check_winner(board, 'O'):
            print("😈 AI wins! Better luck next time.")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
