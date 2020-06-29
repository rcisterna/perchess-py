from itertools import permutations

from perchess.pieces import Piece, Color, Movement


class Knight(Piece):
    """Caballo."""

    def __init__(self, color: Color):
        """
        :param color: Color de jugador.
        """
        movements = []
        side_movements = [1, 2]
        for travel_r, travel_f in permutations(side_movements):
            movements.extend(
                [
                    Movement(travel_r, travel_f),
                    Movement(travel_r, -travel_f),
                    Movement(-travel_r, travel_f),
                    Movement(-travel_r, -travel_f),
                ]
            )
        Piece.__init__(self, color, movements)
