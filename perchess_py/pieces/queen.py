from perchess_py.pieces import Piece, Color, Movement


class Queen(Piece):
    """Reina."""

    def __init__(self, color: Color):
        """
        :param color: Color de jugador.
        """
        movements = []
        for travel in range(1, 8):
            movements.extend(
                [
                    Movement(travel, 0),
                    Movement(travel, travel),
                    Movement(0, travel),
                    Movement(-travel, travel),
                    Movement(-travel, 0),
                    Movement(-travel, -travel),
                    Movement(0, -travel),
                    Movement(travel, -travel),
                ]
            )
        Piece.__init__(self, color, movements)
