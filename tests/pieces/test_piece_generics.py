import random

import pytest

from perchess.exceptions import MovementException
from perchess.pieces import Piece, Color, Movement


def test_init_exceptions():
    with pytest.raises(ValueError):
        Piece(Color.WHITE, [])
    with pytest.raises(ValueError):
        Piece(1, [Movement(1, 1)])


def test_readonly_exceptions():
    piece = Piece(Color.BLACK, [Movement(1, 1)])
    with pytest.raises(AttributeError):
        piece.color = Color.WHITE
    with pytest.raises(AttributeError):
        piece.has_moved = True
    with pytest.raises(AttributeError):
        piece.movements = tuple()


def test_properties():
    color = random.choice([Color.WHITE, Color.BLACK])
    piece = Piece(color, [Movement(1, 1), Movement(-1, -1)])
    assert piece.has_moved is False
    assert piece.color == color
    assert all(a == b for a, b in zip(piece.movements, [Movement(1, 1), Movement(-1, -1)]))

    piece.move(piece.movements[0], None)
    assert piece.has_moved is True


def test_moves():
    color = random.choice([Color.WHITE, Color.BLACK])
    to_capture = Piece(color, [Movement(1, 1)])
    m_normal = Movement(1, 0)
    m_only_first = Movement(1, 0, only_first=True)
    m_only_capture = Movement(1, 0, only_capture=True)
    m_cannot_capture = Movement(1, 0, can_capture=False)
    m_not_added = Movement(-1, 0)
    piece = Piece(color, [m_normal, m_only_first, m_only_capture, m_cannot_capture])

    piece.move(m_only_first, None)
    with pytest.raises(MovementException):
        piece.move(m_only_first, None)
    with pytest.raises(MovementException):
        piece.move(m_not_added, None)
    with pytest.raises(MovementException):
        piece.move(m_only_capture, None)
    piece.move(m_normal, to_capture)
    with pytest.raises(MovementException):
        piece.move(m_cannot_capture, to_capture)
