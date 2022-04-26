import pytest

from utils import double, ticket_price, divide


def test_double():
    assert double(2) == 4


class TestTicketPrice:

    def test_ticket_price_0(self):
        assert ticket_price(0) == "Бесплатно", "Ошибка для 0 лет"


    def test_ticket_price_1(self):
        assert ticket_price(1) == "Бесплатно", "Ошибка для 1 лет"


    def test_ticket_price_7(self):
        assert ticket_price(7) == "100 рублей", "Ошибка для 7 лет"


    def test_ticket_price_18(self):
        assert ticket_price(18) == "200 рублей", "Ошибка для 18 лет"


    def test_ticket_price_25(self):
        assert ticket_price(25) == "300 рублей", "Ошибка для 25 лет"


    def test_ticket_price_60(self):
        assert ticket_price(60) == "Бесплатно", "Ошибка для 60 лет"


    def test_ticket_price_minus_1(self):
        assert ticket_price(-1) == "Ошибка", "Ошибка для -1 лет"


def test_positive_int():
    assert divide(100, 10) == 10.0

def test_negative_int():
    assert divide(-20, -5) == 4.0

def test_zero_to_int():
    assert divide(0, 2) == 0.0

def test_float():
    assert divide(2.2, 2) == 1.1

def test_type_mismatch():
    with pytest.raises(TypeError):
        divide(True, None)

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(100, 0)


import pytest

from utils import get_verbal_grade

grade_parameters = [
    (2, "Плохо"),
    (3, "Удовлетворительно"),
    (4, "Хорошо"),
    (5, "Отлично"),
]


@pytest.mark.parametrize("grade_int, grade_str", grade_parameters)
def test_get_verbal_grade(grade_int, grade_str):
    assert get_verbal_grade(grade_int) == grade_str


grade_exceptions = [
    (1, ValueError),
    (6, ValueError),
    ("5", TypeError),
    (5.0, TypeError)
]


@pytest.mark.parametrize("grade_int, exception", grade_exceptions)
def test_get_verbal_grade_exceptions(grade_int, exception):
    with pytest.raises(exception):
        assert get_verbal_grade(grade_int)


from utils import get_period

period_parameters = [(6, "ночь"), (8, "утро"), (17, "день"), (19, "вечер")]

@pytest.mark.parametrize("hour, period", period_parameters)
def test_get_period(hour, period):
    assert get_period(hour) == period

period_exceptions = [("5", TypeError), (26, ValueError)]

@pytest.mark.parametrize("hour, exception", period_exceptions)
def test_get_period_exceptions(hour, exception):
    with pytest.raises(exception):
        assert get_period(hour)





