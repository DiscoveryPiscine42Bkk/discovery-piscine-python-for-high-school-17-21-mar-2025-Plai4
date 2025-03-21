def is_king_in_check(board):
    # Find the King's position
    king_position = None
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_position = (i, j)
                break
        if king_position:
            break

    if not king_position:
        print("Error: King not found!")
        return

    king_x, king_y = king_position

    # Directions for rooks and queens (vertical and horizontal)
    rook_queen_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Directions for bishops and queens (diagonal)
    bishop_queen_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def is_on_board(x, y):
        return 0 <= x < len(board) and 0 <= y < len(board)

    # Check for Rooks, Queens (Horizontal & Vertical)
    for dx, dy in rook_queen_directions:
        x, y = king_x, king_y
        while True:
            x += dx
            y += dy
            if not is_on_board(x, y):
                break
            piece = board[x][y]
            if piece != ' ':
                if (piece == 'R' or piece == 'Q'):  # Enemy rook or queen
                    print("Success")
                    return
                break  # Blocked by another piece
    # Check for Bishops, Queens (Diagonal)
    for dx, dy in bishop_queen_directions:
        x, y = king_x, king_y
        while True:
            x += dx
            y += dy
            if not is_on_board(x, y):
                break
            piece = board[x][y]
            if piece != ' ':
                if (piece == 'B' or piece == 'Q'):  # Enemy bishop or queen
                    print("Success")
                    return
                break  # Blocked by another piece

    # Check for Pawns (Pawns only attack diagonally, and only one step away)
    pawn_attack_positions = [(king_x - 1, king_y - 1), (king_x - 1, king_y + 1), 
                             (king_x + 1, king_y - 1), (king_x + 1, king_y + 1)]
    for x, y in pawn_attack_positions:
        if is_on_board(x, y):
            if board[x][y] == 'P':  # Enemy pawn
                print("Success")
                return

    print("Fail")

# Example Test
board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'K', ' ', ' ', ' ', ' '],  # King is at (3, 3)
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],  # Pawn at (5, 3) attacking the king
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

is_king_in_check(board)