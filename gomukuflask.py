import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Existing functions from your script
def create_board(size):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board

def is_occupied(board, position):
    row_value, colum_value = position
    row_value = int(row_value)
    colum_value = (ord(colum_value.upper()) - ord('A'))
    if board[row_value][colum_value] != " ":
        return True
    else:
        return False

def place_on_board(board, stone, position):
    row_value, colum_value = position
    row_value = int(row_value)
    colum_value = (ord(colum_value.upper()) - ord('A'))
    if board[row_value][colum_value] == ' ':
        board[row_value][colum_value] = stone
        return True
    else:
        return False

def print_board(board):
    for row in board:
        print(' '.join(row))
    print('-' * (len(board) * 2 - 1))

def check_available_moves(board):
    moves = []
    for row in range(len(board)):
        for colum in range(len(board[0])):
            if board[row][colum] == " ":
                moves.append(f"{row}{chr(colum + 65)}")
    return moves

def check_for_winner(board):
    size = len(board)
    if check_available_moves(board) != 0:
        for colum in range(size-4):
            for row in range(size):
                if board[row][colum] == "●" and board[row][colum + 1] == "●" and board[row][colum + 2] == "●" and board[row][colum + 3] == "●" and board[row][colum + 4] == "●":
                    return "●"
                elif board[row][colum] == "o" and board[row][colum + 1] == "o" and board[row][colum + 2] == "o" and board[row][colum + 3] == "o" and board[row][colum + 4] == "o":
                    return "o"
        for colum in range(size):
            for row in range(size-4):
                if board[row][colum] == "●" and board[row + 1][colum] == "●" and board[row + 2][colum] == "●" and board[row + 3][colum] == "●" and board[row + 4][colum] == "●":
                    return "●"
                elif board[row][colum] == "o" and board[row + 1][colum] == "o" and board[row + 2][colum] == "o" and board[row + 3][colum] == "o" and board[row + 4][colum] == "o":
                    return "o"
        for colum in range(size-4):
            for row in range(size-4):
                if board[row][colum] == "●" and board[row + 1][colum + 1] == "●" and board[row + 2][colum + 2] == "●" and board[row + 3][colum + 3] == "●" and board[row + 4][colum + 4] == "●":
                    return "●"
                elif board[row][colum] == "o" and board[row + 1][colum + 1] == "o" and board[row + 2][colum + 2] == "o" and board[row + 3][colum + 3] == "o" and board[row + 4][colum + 4] == "o":
                    return "o"
        for row in range(size-4):
            for colum in range(size-4):
                if board[row][colum] == "●" and board[row - 1][colum + 1] == "●" and board[row - 2][colum + 2] == "●" and board[row - 3][colum + 3] == "●" and board[row - 4][colum + 4] == "●":
                    return "●"
                elif board[row][colum] == "o" and board[row - 1][colum + 1] == "o" and board[row - 2][colum + 2] == "o" and board[row - 3][colum + 3] == "o" and board[row - 4][colum + 4] == "o":
                    return "o"
    elif check_available_moves(board) == 0:
        return "Draw"
    else:
        return "None"

def random_computer_player(board, player_move):
    comp_moves = []
    size = len(board)
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == 0 and c == 0:
                continue
            row = int(player_move[0]) + r
            colum = (ord(player_move[1].upper()) - 65) + c
            if 0 <= row < size and 0 <= colum < size and board[row][colum] == " ":
                colum = chr(65 + colum)
                comp_moves.append((str(row), str(colum)))
    if len(comp_moves) != 0:
        random_comp_move = random.choice(comp_moves)
    else:
        random_comp_move = random.choice(check_available_moves(board))
    return random_comp_move

# Global variables to store the board and game mode
board = None
player_mode = None

@app.route('/start_game', methods=['POST'])
def start_game():
    global board, player_mode
    size = request.json.get('size', 9)
    player_mode = request.json.get('player_mode', 1)
    board = create_board(size)
    return jsonify({"message": "Game started", "board": board, "player_mode": player_mode})

@app.route('/place_stone', methods=['POST'])
def place_stone():
    global board, player_mode
    stone = request.json.get('stone')
    position = request.json.get('position')
    if place_on_board(board, stone, position):
        winner = check_for_winner(board)
        if player_mode == 2 and stone == "●" and winner is None:
            # Computer's turn
            comp_move = random_computer_player(board, position)
            place_on_board(board, "o", comp_move)
            winner = check_for_winner(board)
            return jsonify({"message": "Stone placed", "board": board, "winner": winner, "comp_move": comp_move})
        return jsonify({"message": "Stone placed", "board": board, "winner": winner})
    else:
        return jsonify({"message": "Invalid move"}), 400

@app.route('/print_board', methods=['GET'])
def get_board():
    global board
    return jsonify({"board": board})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)