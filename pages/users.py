from dataclasses import dataclass


@dataclass
class Users:
    """Пользователи эталона"""
    login: str
    password: str


admin = Users('b.pogodin', '68f1d85b')
jerry = Users('jerry_smith', '123456')
# morty = Users()
# summer= Users()
# beth= Users()
