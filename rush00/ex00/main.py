# Chess game in Python

class ChessBoard:
    def __init__(self):
        # Initialize the board with standard chess pieces
        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
        self.current_player = 'white'

    def display_board(self):
        # Print the board with row and column labels
        print("  a b c d e f g h")
        for i, row in enumerate(self.board):
            print(8 - i, end=' ')
            for cell in row:
                print(cell, end=' ')
            print(8 - i)
        print("  a b c d e f g h")

    def get_position(self, pos):
        # Convert chess notation (e.g., 'e4') to board indices
        col = ord(pos[0]) - ord('a')
        row = 8 - int(pos[1])
        return row, col

    def is_valid_move(self, start, end):
        # Check if the move is valid (basic implementation)
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]
        target = self.board[end_row][end_col]

        # Basic rules (simplified for demonstration)
        if piece == ' ':
            return False  # No piece to move
        if (piece.isupper() and self.current_player == 'black') or (piece.islower() and self.current_player == 'white'):
            return False  # Wrong player's piece
        if target != ' ' and (target.isupper() == piece.isupper()):
            return False  # Cannot capture your own piece

        # Add more rules for specific pieces (e.g., pawn, rook, etc.)
        return True

    def make_move(self, start_pos, end_pos):
        # Move a piece on the board
        start = self.get_position(start_pos)
        end = self.get_position(end_pos)

        if not self.is_valid_move(start, end):
            print("Invalid move!")
            return False

        # Perform the move
        piece = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = ' '
        self.board[end[0]][end[1]] = piece

        # Switch players
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        return True

    def play(self):
        # Main game loop
        while True:
            self.display_board()
            print(f"{self.current_player.capitalize()}'s turn")
            move = input("Enter your move (e.g., 'e2 e4'): ")
            start_pos, end_pos = move.split()
            if self.make_move(start_pos, end_pos):
                print("Move successful!")
            else:
                print("Try again.")

# Run the game
if __name__ == "__main__":
    game = ChessBoard()
    game.play()