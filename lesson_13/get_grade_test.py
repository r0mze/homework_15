from get_grade_function import get_grade

import pytest

grade_parameters = [
    (10, 2),
    (30, 3),
    (50, 4),
    (90, 5),
]


@pytest.mark.parametrize("grade_received, grade_equivalent", grade_parameters)
def test_get_grade(grade_received, grade_equivalent):
    assert get_grade(grade_received) == grade_equivalent


grade_exceptions = {
    (-1, ValueError),
    (101, ValueError),
    ("5", TypeError),
    (5.0, TypeError)
}


@pytest.mark.parametrize("grade_received, exception", grade_exceptions)
def test_get_grade_exceptions(grade_received, exception):
    with pytest.raises(exception):
        assert get_grade(grade_received)