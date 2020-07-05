from typing import Dict, Optional

from perchess import pieces


class Board:
    """Tablero de ajedrez."""

    FILES = ["a", "b", "c", "d", "e", "f", "g", "h"]
    RANKS = ["1", "2", "3", "4", "5", "6", "7", "8"]

    PIECE_CLASS_BY_FILE = {
        'a': pieces.Rook,
        'b': pieces.Knight,
        'c': pieces.Bishop,
        'd': pieces.Queen,
        'e': pieces.King,
        'f': pieces.Bishop,
        'g': pieces.Knight,
        'h': pieces.Rook,
    }

    def __init__(self):
        self.__pos_by_piece: Dict[pieces.Piece, str] = {}
        self.__piece_by_pos: Dict[str, Optional[pieces.Piece]] = {}
        self.__set_initial_positions()
        self.__set_initial_player(pieces.Colors.WHITE)
        self.__set_initial_player(pieces.Colors.BLACK)

    def __set_initial_positions(self):
        for file in self.FILES:
            for rank in self.RANKS:
                self.__piece_by_pos[file + rank] = None

    def __set_initial_player(self, color: pieces.Colors):
        rank_major = '1' if color == pieces.Colors.WHITE else '8'
        rank_pawns = '2' if color == pieces.Colors.WHITE else '7'
        for file in self.FILES:
            piece_class = self.PIECE_CLASS_BY_FILE[file]
            self.__set_initial_piece(pieces.Pawn(color), file + rank_pawns)
            self.__set_initial_piece(piece_class(color), file + rank_major)

    def __set_initial_piece(self, piece: pieces.Piece, pos: str):
        self.__pos_by_piece[piece] = pos
        self.__piece_by_pos[pos] = piece
