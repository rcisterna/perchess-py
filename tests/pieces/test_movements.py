import random

import pytest

from perchess.pieces import Movement


def test_init_exceptions():
    with pytest.raises(ValueError):
        Movement(0, 0)
    with pytest.raises(ValueError):
        Movement(1, 1, only_capture=True, can_capture=False)
    with pytest.raises(ValueError):
        Movement(8, 0)
    with pytest.raises(ValueError):
        Movement(-8, 0)
    with pytest.raises(ValueError):
        Movement(0, 8)
    with pytest.raises(ValueError):
        Movement(0, -8)


def test_readonly_exceptions():
    mov = Movement(1, 1)
    with pytest.raises(AttributeError):
        mov.file = 2
    with pytest.raises(AttributeError):
        mov.rank = 2
    with pytest.raises(AttributeError):
        mov.only_first = True
    with pytest.raises(AttributeError):
        mov.only_capture = True
    with pytest.raises(AttributeError):
        mov.can_capture = True


def test_properties():
    travel_values = {i for i in range(-7, 8)}
    travel_values.discard(0)
    file, rank = random.sample(travel_values, 2)
    only_first = random.choice([True, False])
    only_capture = random.choice([True, False])
    can_capture = True if only_capture else random.choice([True, False])

    mov = Movement(file, rank, only_first, only_capture, can_capture)
    assert mov.file == file
    assert mov.rank == rank
    assert mov.only_first == only_first
    assert mov.only_capture == only_capture
    assert mov.can_capture == can_capture


def test_equality():
    mov = Movement(1, 1)
    assert mov == Movement(mov.file, mov.rank, mov.only_first, mov.only_capture, mov.can_capture)
    assert mov != Movement(-mov.file, mov.rank, mov.only_first, mov.only_capture, mov.can_capture)
    assert mov != Movement(mov.file, -mov.rank, mov.only_first, mov.only_capture, mov.can_capture)
    assert mov != Movement(mov.file, mov.rank, not mov.only_first, mov.only_capture, mov.can_capture)
    assert mov != Movement(mov.file, mov.rank, mov.only_first, not mov.only_capture, mov.can_capture)
    assert mov != Movement(mov.file, mov.rank, mov.only_first, mov.only_capture, not mov.can_capture)
    assert mov != 1
