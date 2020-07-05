from typing import Optional

from perchess.pieces import Piece


class Movement:
    """Movimiento en el tablero."""

    def __init__(self, orig: str, dest: str, moving: Piece, captured: Optional[Piece] = None):
        self.__orig = orig
        self.__dest = dest
        self.__moving = moving
        self.__captured = captured

    @property
    def orig(self) -> str:
        """Nombre de la casilla de origen."""
        return self.__orig

    @property
    def dest(self) -> str:
        """Nombre de la casilla de destino."""
        return self.__dest

    @property
    def moving(self) -> Piece:
        """Pieza que realiza el movimiento."""
        return self.__moving

    @property
    def captured(self) -> Piece:
        """Pieza capturada en el movimiento."""
        return self.__captured
