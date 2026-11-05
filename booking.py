"""Модуль розрахунку вартості бронювання з промокодом (HBK-13)."""

PROMO_CODES = {
    "SUMMER10": 10,
    "WELCOME15": 15,
    "VIP20": 20,
}


def booking_total(price_per_night, nights, promo_code=None):
    """Повертає вартість проживання з урахуванням промокоду.

    price_per_night -- ціна за ніч (> 0)
    nights          -- кількість ночей (ціле число >= 1)
    promo_code      -- необов'язковий промокод
    """
    if isinstance(price_per_night, bool) or not isinstance(price_per_night, (int, float)):
        raise TypeError("Ціна має бути числом")
    if isinstance(nights, bool) or not isinstance(nights, int):
        raise TypeError("Кількість ночей має бути цілим числом")
    if price_per_night <= 0:
        raise ValueError("Ціна має бути більшою за 0")
    if nights < 1:
        raise ValueError("Кількість ночей має бути не менше 1")

    total = price_per_night * nights

    if promo_code is not None:
        code = str(promo_code).strip().upper()
        if code not in PROMO_CODES:
            raise ValueError("Недійсний промокод")
        total = total * (100 - PROMO_CODES[code]) / 100

    return round(total, 2)
