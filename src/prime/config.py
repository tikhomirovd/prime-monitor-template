"""Подключение к учебной базе ПРАЙМ.

Строка подключения живёт в файле .env, а не в коде. Причина простая:
ноутбук вы покажете преподавателю, выложите на GitHub, отправите
однокурснику — и пароль поедет вместе с ним. Файл .env закрыт
в .gitignore и не уедет никуда.
"""

import os

from dotenv import find_dotenv, load_dotenv
from sqlalchemy import Engine, create_engine


def get_engine() -> Engine:
    """Вернуть движок SQLAlchemy к базе ПРАЙМ.

    Файл .env ищется вверх по дереву от текущей папки, поэтому функция
    работает и из корня проекта, и из notebooks/.
    """
    load_dotenv(find_dotenv(usecwd=True))

    dsn = os.environ.get("PRIME_DSN")
    if not dsn:
        raise RuntimeError(
            "Не найдена переменная PRIME_DSN. "
            "Скопируйте .env.example в .env и впишите строку, "
            "которую выдал бот курса по команде /db."
        )

    return create_engine(dsn)
