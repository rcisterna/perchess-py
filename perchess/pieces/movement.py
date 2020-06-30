class Movement:
    """Descriptor de movimiento."""

    def __init__(
        self, file: int, rank: int, only_first: bool = False, only_capture: bool = False, can_capture: bool = True
    ):
        """
        :param file: Movimiento en la columna.
        :param rank: Movimiento en la fila.
        :param only_first: Indica si es solo el primer movimiento.
        :param only_capture: Indica si es solo para captura.
        :param can_capture: Indica si puede capturar.
        """
        if only_capture and not can_capture:
            raise ValueError("No se puede definir movimiento de solo captura y que no puede capturar.")
        if not file and not rank:
            raise ValueError("No se puede definir movimiento que no desplaza la pieza.")
        if abs(file) > 7 or abs(rank) > 7:
            raise ValueError("No se puede definir movimiento que desplace la pieza más de 7 casillas.")
        self.__file = file
        self.__rank = rank
        self.__only_first = only_first
        self.__only_capture = only_capture
        self.__can_capture = can_capture

    @property
    def file(self) -> int:
        """Movimientos en la columna."""
        return self.__file

    @property
    def rank(self) -> int:
        """Movimientos en la fila."""
        return self.__rank

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

    def __eq__(self, other):
        if not isinstance(other, Movement):
            return False
        return (
            self.file == other.file
            and self.rank == other.rank
            and self.only_first == other.only_first
            and self.only_capture == other.only_capture
            and self.can_capture == other.can_capture
        )
