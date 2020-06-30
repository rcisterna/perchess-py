from typing import Iterable, Tuple, Optional

from perchess.exceptions import MovementException
from perchess.pieces import Movement, Colors


class Piece:
    """Pieza de ajedrez."""

    def __init__(self, color: Colors, movements: Iterable[Movement]):
        """
        :param color: Color de jugador.
        :param movements: Movimientos de la pieza.
        """
        if not isinstance(color, Colors):
            raise ValueError("Color de la pieza debe ser instancia de la enumeración de colores.")
        self.__movements = tuple(m for m in movements)
        if not len(self.__movements):
            raise ValueError("La pieza debe tener movimientos.")
        self.__has_moved = False
        self.__color = color

    @property
    def has_moved(self) -> int:
        """Indica si la pieza se ha movido."""
        return self.__has_moved

    @property
    def color(self) -> Colors:
        """Indica el color de la pieza."""
        return self.__color

    @property
    def movements(self) -> Tuple[Movement, ...]:
        """Contiene los movimientos de la pieza."""
        return self.__movements

    def move(self, movement: Movement, capturing: Optional["Piece"]):
        """
        Mueve la pieza.

        :param movement: Movimiento que realizará la pieza.
        :param capturing: Pieza que está en la casilla en que se moverá esta pieza.
        """
        if movement not in self.movements:
            raise MovementException("La pieza no tiene este movimiento.")
        if movement.only_first and self.has_moved:
            raise MovementException("La pieza ya se movió.")
        if capturing and not movement.can_capture:
            raise MovementException("La pieza no puede capturar con este movimiento.")
        if not capturing and movement.only_capture:
            raise MovementException("La pieza solo puede capturar con este movimiento.")
        self.__has_moved = True
