from dataclasses import dataclass


@dataclass
class StableUsers:
    """Пользователи эталона"""
    login: str
    password: str


admin = StableUsers('b.pogodin', '68f1d85b')
jerry = StableUsers('jerry_smith', '123456')
# morty = StableUsers()
# summer= StableUsers()
# beth= StableUsers()

