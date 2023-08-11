from dataclasses import dataclass


@dataclass
class StableUsers:
    """Пользователи эталона"""
    login: str
    password: str


admin = StableUsers('b.pogodin', '3678vg')
minervakms = StableUsers('ricksanchez', 'minervakms') # при смене - заменить в data_login_password
andrey = StableUsers('andrey', '10f0b265')  # при смене - заменить в DataLoginPassword
person1 = StableUsers('person1', '777qwerty')
person2 = StableUsers('person2', '777qwerty')
person3 = StableUsers('person3', '777qwerty')
person4 = StableUsers('person4', '777qwerty')


class DataLoginPassword:

    @staticmethod
    def correct_data():
        login = 'ricksanchez'
        password = 'minervakms'
        return login, password
    @staticmethod
    def incorrect_data():
        login_incorrect = 'm.andreyq'
        password_incorrect = '395a5555'
        return login_incorrect, password_incorrect

"""title"""
name_project ='selen'
name_ = 'Весь контент'
# base_url = "https://test6.minervasoft.ru/"


"""текст для поиска на английском и русском"""
text_ru = "С другой стороны курс на социально-ориентированный национальный проект обеспечивает актуальность " \
          "дальнейших направлений развитая системы массового участия. Соображения высшего порядка, а также " \
          "дальнейшее развитие различных форм деятельности в значительной степени обуславливает создание " \
          "существующих финансовых и административных условий?"

text_en = "A lot of the central bank news is priced into equities and investors are now taking a step back" \
          " to evaluate why central banks have turned more dovish, said David Holohan, a strategist at Mediolanum" \
          " Asset Management in Dublin."