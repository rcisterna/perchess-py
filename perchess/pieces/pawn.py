from perchess.pieces import Movement, Color, Piece


class Pawn(Piece):
    """Peón."""

    def __init__(self, color: Color):
        """
        :param color: Color de jugador.
        """
        forward = 1 if color == Color.WHITE else -1
        movements = [
            Movement(0, forward, can_capture=False),
            Movement(0, forward * 2, only_first=True, can_capture=False),
            Movement(-1, forward, only_capture=True),
            Movement(1, forward, only_capture=True),
        ]
        Piece.__init__(self, color, movements)
