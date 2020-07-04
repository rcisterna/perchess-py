from perchess.pieces import Piece, Colors, Movement


class King(Piece):
    """Rey."""

    def __init__(self, color: Colors):
        """
        :param color: Color de jugador.
        """
        movements = [
            Movement(1, 0),
            Movement(1, 1),
            Movement(0, 1),
            Movement(-1, 1),
            Movement(-1, 0),
            Movement(-1, -1),
            Movement(0, -1),
            Movement(1, -1),
        ]
        Piece.__init__(self, "K", color, movements)
