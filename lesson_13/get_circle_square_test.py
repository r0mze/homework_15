import pytest

import pytest

from utils import get_circle_square

def test_get_circle_square_normal():
    square = get_circle_square(1)
    assert round(square, 2) == 3.14

def test_get_circle_square_normal():
    square = get_circle_square(3)
    assert round(square, 2) == 28.27

def test_get_circle_square_value_error():
    with pytest.raises(ValueError):
        get_circle_square(-2)

def test_get_circle_square_type_error():
    with pytest.raises(TypeError):
        get_circle_square("2")
