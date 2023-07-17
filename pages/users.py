from dataclasses import dataclass


@dataclass
class StableUsers:
    """Пользователи эталона"""
    login: str
    password: str


admin = StableUsers('b.pogodin', '68f1d85b')
minervakms = StableUsers('minervakms', 'minervakms')
person1 = StableUsers('person1', '777qwerty')
person2 = StableUsers('person2', '777qwerty')
person3 = StableUsers('person3', '777qwerty')
person4 = StableUsers('person4', '777qwerty')

