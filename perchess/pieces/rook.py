from perchess.pieces import Piece, Colors, Movement


class Rook(Piece):
    """Torre."""

    def __init__(self, color: Colors):
        """
        :param color: Color de jugador.
        """
        movements = []
        for travel in range(1, 8):
            movements.extend([Movement(travel, 0), Movement(-travel, 0), Movement(0, travel), Movement(0, -travel)])
        Piece.__init__(self, color, movements)
