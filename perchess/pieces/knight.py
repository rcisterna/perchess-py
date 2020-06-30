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
        for travel_f, travel_r in permutations(side_movements):
            movements.extend(
                [
                    Movement(travel_f, travel_r),
                    Movement(travel_f, -travel_r),
                    Movement(-travel_f, travel_r),
                    Movement(-travel_f, -travel_r),
                ]
            )
        Piece.__init__(self, color, movements)
