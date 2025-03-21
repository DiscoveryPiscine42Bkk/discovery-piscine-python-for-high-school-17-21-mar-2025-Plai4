class GameState:
    # other methods / properties

    @property
    def legal_moves(self) -> Iterable[Move]: 
        """Finds all legal Moves for the current Player (also considers check)"""
        # TODO: implement

    @property
    def is_check(self) -> bool:
        """Checks if the last move was a check (or checkmate)"""
        # TODO: implement

    @property
    def is_checkmate(self) -> bool:
        """Checks if the last move was a checkmate"""

        if not self.is_check:
            return False  # If the last move was not a check, it also wasn't a checkmate
        for move in self.legal_moves():
            return False  # There exists at least one move that gets the player out of check
        return True  # No move gets the player get out of check, so therefore they are checkmate