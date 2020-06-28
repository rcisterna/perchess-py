from typing import Iterable

from perchess_py.exceptions import MovementException
from perchess_py.pieces import Movement, Color


class Piece:
    """Pieza de ajedrez."""

    def __init__(self, color: Color, movements: Iterable[Movement]):
        self.__has_moved = False
        self.__color = color
        self.movements = tuple(m for m in movements)

    @property
    def has_moved(self) -> int:
        """Indica si la pieza se ha movido."""
        return self.__has_moved

    @property
    def color(self) -> Color:
        """Indica el color de la pieza."""
        return self.__color

    def move(self, movement: Movement, capturing: "Piece"):
        if movement not in self.movements:
            raise MovementException("La pieza no tiene este movimiento.")
        if movement.only_first and self.has_moved:
            raise MovementException("La pieza ya se movió.")
        if capturing and not movement.can_capture:
            raise MovementException("La pieza no puede capturar con este movimiento.")
        if not capturing and not movement.only_capture:
            raise MovementException("La pieza solo puede capturar con este movimiento.")
        self.__has_moved = True
