from perchess.pieces import Movement, Colors, Piece


class Pawn(Piece):
    """Peón."""

    def __init__(self, color: Colors):
        """
        :param color: Color de jugador.
        """
        forward = 1 if color == Colors.WHITE else -1
        movements = [
            Movement(0, forward, can_capture=False),
            Movement(0, forward * 2, only_first=True, can_capture=False),
            Movement(-1, forward, only_capture=True),
            Movement(1, forward, only_capture=True),
        ]
        Piece.__init__(self, color, movements)
