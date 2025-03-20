def is_checkmate(board, player):
    # Step 1: Check if the player's king is in check
    if not is_in_check(board, player):
        return False  # Not checkmate if the king is not in check

    # Step 2: Generate all possible moves for the player
    for move in generate_legal_moves(board, player):
        # Simulate the move
        new_board = make_move(board, move)
        # Check if the king is still in check after the move
        if not is_in_check(new_board, player):
            return False  # The player can escape check, so it's not checkmate

    # Step 3: If no moves escape check, it's checkmate
    return True

def is_in_check(board, player):
    king_position = find_king(board, player)
    # Check if any opponent's piece attacks the king's position
    for opponent_move in generate_opponent_attacks(board, player):
        if opponent_move.target == king_position:
            return True
    return False