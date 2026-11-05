import pytest
from booking import booking_total


# КП1: сума без промокоду = ціна * ночі
def test_total_without_promo():
    assert booking_total(100, 3) == 300


# КП2: дійсний промокод дає знижку у відсотках
def test_total_with_valid_promo():
    assert booking_total(100, 2, "SUMMER10") == 180


@pytest.mark.parametrize("code, expected", [
    ("SUMMER10", 900),
    ("WELCOME15", 850),
    ("VIP20", 800),
])
def test_all_promo_codes(code, expected):
    assert booking_total(100, 10, code) == expected


# КП3: недійсний промокод
def test_invalid_promo_raises():
    with pytest.raises(ValueError):
        booking_total(100, 2, "FAKE99")


# КП4: промокод нечутливий до регістру та пробілів
def test_promo_case_and_spaces_ignored():
    assert booking_total(100, 2, "  summer10 ") == 180


# Граничний випадок: мінімальна кількість ночей
def test_minimum_one_night():
    assert booking_total(50, 1) == 50


# Граничний випадок: округлення до 2 знаків
def test_rounding_two_decimals():
    assert booking_total(33.33, 3, "WELCOME15") == 84.99


# Некоректні вхідні дані
@pytest.mark.parametrize("price, nights", [(0, 2), (-10, 2), (100, 0), (100, -1)])
def test_invalid_price_or_nights(price, nights):
    with pytest.raises(ValueError):
        booking_total(price, nights)


def test_wrong_types():
    with pytest.raises(TypeError):
        booking_total("100", 2)
    with pytest.raises(TypeError):
        booking_total(100, 2.5)
