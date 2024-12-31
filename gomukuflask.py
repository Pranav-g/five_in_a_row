import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Existing functions from your script
def create_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]

def is_occupied(board, position):
    row, col = position
    row = int(row)
    col = ord(col.upper()) - ord('A')
    return board[row][col] != " "

def place_on_board(board, stone, position):
    row, col = position
    row = int(row)
    col = ord(col.upper()) - ord('A')
    if board[row][col] == ' ':
        board[row][col] = stone
        return True
    return False

def print_board(board):
    return [' '.join(row) for row in board]

def check_available_moves(board):
    moves = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == " ":
                moves.append(f"{row}{chr(col + 65)}")
    return moves

def check_for_winner(board):
    size = len(board)
    for row in range(size):
        for col in range(size - 4):
            if board[row][col] != " " and all(board[row][col + i] == board[row][col] for i in range(5)):
                return board[row][col]

    for row in range(size - 4):
        for col in range(size):
            if board[row][col] != " " and all(board[row + i][col] == board[row][col] for i in range(5)):
                return board[row][col]

    for row in range(size - 4):
        for col in range(size - 4):
            if board[row][col] != " " and all(board[row + i][col + i] == board[row][col] for i in range(5)):
                return board[row][col]

    for row in range(4, size):
        for col in range(size - 4):
            if board[row][col] != " " and all(board[row - i][col + i] == board[row][col] for i in range(5)):
                return board[row][col]

    if not any(" " in row for row in board):
        return "Draw"

    return None

def random_computer_player(board, player_move):
    moves = check_available_moves(board)
    return random.choice(moves) if moves else None

# Global variables
board = None
player_mode = None

@app.route('/start_game', methods=['POST'])
def start_game():
    global board, player_mode
    size = request.json.get('size', 9)
    player_mode = request.json.get('player_mode', 1)
    board = create_board(size)
    return jsonify({
        "message": "Game started",
        "board": print_board(board),
        "available_moves": check_available_moves(board),
        "player_mode": player_mode
    })

@app.route('/place_stone', methods=['POST'])
def place_stone():
    global board, player_mode
    stone = request.json.get('stone')
    position = request.json.get('position')
    if place_on_board(board, stone, position):
        winner = check_for_winner(board)
        if winner:
            return jsonify({"message": f"{winner} wins!", "board": print_board(board)})

        if player_mode == 2 and stone == "●":
            comp_move = random_computer_player(board, position)
            place_on_board(board, "o", (comp_move[0], comp_move[1]))
            winner = check_for_winner(board)
            return jsonify({
                "message": "Move placed",
                "board": print_board(board),
                "available_moves": check_available_moves(board),
                "comp_move": comp_move,
                "winner": winner
            })

        return jsonify({
            "message": "Move placed",
            "board": print_board(board),
            "available_moves": check_available_moves(board),
            "winner": winner
        })
    else:
        return jsonify({"message": "Invalid move"}), 400

@app.route('/get_board', methods=['GET'])
def get_board():
    global board
    return jsonify({
        "board": print_board(board),
        "available_moves": check_available_moves(board)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
