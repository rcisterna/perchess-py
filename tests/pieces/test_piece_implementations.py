import random

import pytest

from perchess.pieces import Colors, Pawn, Knight, Bishop, Rook, King, Queen

COLORS = [Colors.WHITE, Colors.BLACK]


@pytest.mark.parametrize("color", COLORS)
def test_pawn(color):
    pawn = Pawn(color)
    for m in pawn.movements:
        assert m.rank > 0 if color == Colors.WHITE else m.rank < 0
        assert m.only_capture is True if m.file else m.can_capture is False


def test_knight():
    knight = Knight(random.choice(COLORS))
    for m in knight.movements:
        knight.move(m, None)


def test_bishop():
    bishop = Bishop(random.choice(COLORS))
    for m in bishop.movements:
        bishop.move(m, None)


def test_rook():
    rook = Rook(random.choice(COLORS))
    for m in rook.movements:
        rook.move(m, None)


def test_queen():
    queen = Queen(random.choice(COLORS))
    for m in queen.movements:
        queen.move(m, None)


def test_king():
    king = King(random.choice(COLORS))
    for m in king.movements:
        king.move(m, None)
