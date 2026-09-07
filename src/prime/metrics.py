"""Метрики подписки ПРАЙМ.

Пока всё на чистом Python: pandas начинается с темы 03. Функции здесь
принимают список словарей — ровно то, что отдаёт база через fetchall()
и что приходит из внешнего API.
"""


def revenue(payments: list[dict]) -> float:
    """Выручка: сумма списаний."""
    return sum(p["amount"] for p in payments)
