from perchess_py.pieces import Piece, Color, Movement


class Bishop(Piece):
    """Alfil."""

    def __init__(self, color: Color):
        """
        :param color: Color de jugador.
        """
        movements = []
        for travel in range(1, 8):
            movements.extend(
                [
                    Movement(travel, travel),
                    Movement(travel, -travel),
                    Movement(-travel, travel),
                    Movement(-travel, -travel),
                ]
            )
        Piece.__init__(self, color, movements)
