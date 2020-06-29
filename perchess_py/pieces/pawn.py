from perchess_py.pieces import Movement, Color, Piece


class Pawn(Piece):
    """Peón."""

    def __init__(self, color: Color):
        """
        :param color: Color de jugador.
        """
        forward = 1 if color == Color.WHITE else -1
        movements = [
            Movement(forward, 0, can_capture=False),
            Movement(forward * 2, 0, only_first=True, can_capture=False),
            Movement(forward, -1, only_capture=True),
            Movement(forward, 1, only_capture=True),
        ]
        Piece.__init__(self, color, movements)
