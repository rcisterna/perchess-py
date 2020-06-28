from perchess_py.exceptions import MovementException


class Movement:
    """Descriptor de movimiento."""

    def __init__(
        self, rank: int, file: int, only_first: bool = False, only_capture: bool = False, can_capture: bool = True
    ):
        """
        :param rank: Movimiento en la fila.
        :param file: Movimiento en la columna.
        :param only_first: Indica si es solo el primer movimiento.
        :param only_capture: Indica si es solo para captura.
        :param can_capture: Indica si puede capturar.
        """
        if only_capture and not can_capture:
            raise MovementException("No se puede definir movimiento de solo captura y que no puede capturar.")
        if not rank and not file:
            raise MovementException("No se puede definir movimiento que no desplaza la pieza.")
        self.__rank = rank
        self.__file = file
        self.__only_first = only_first
        self.__only_capture = only_capture
        self.__can_capture = can_capture

    @property
    def rank(self) -> int:
        """Movimientos en la fila."""
        return self.__rank

    @property
    def file(self) -> int:
        """Movimientos en la columna."""
        return self.__file

    @property
    def only_first(self) -> bool:
        """Indica si es solo primer movimiento."""
        return self.__only_first

    @property
    def only_capture(self) -> bool:
        """Indica si es solo movimiento de captura."""
        return self.__only_capture

    @property
    def can_capture(self) -> bool:
        """Indica si puede capturar."""
        return self.__can_capture
