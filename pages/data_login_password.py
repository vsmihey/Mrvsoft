# верные данные
import os
from pages.users import StableUsers

# login = input("введите логин (без кавычек): ")  #'m.andrey'
# login = 'andrey'
# password = '004e9f86'
# password = input("введите пароль (без кавычек): ")  #'e70a8e89'
# password = 'ricksanchez'

# Учетка Бориса
# login = 'b.pogodin'
# password = '68f1d85b'
login = 'ricksanchez'
password = 'ricksanchez'

# неверные данные
# login_incorrect = 'm.andreyq'
# password_incorrect = '395a5555'
# url
# url = 'https://test6.minervasoft.ru'
url = 'https://test-auto.minervasoft.ru/'
user = StableUsers('boris', '367836')

# url = 'https://test2.minervasoft.ru/login?from=%2F'
# url = input("введите url адрес (без кавычек): ")

# url = 'https://dev-5811.t5.minervasoft.ru/login?from=%2F'
# base_url = "https://test6.minervasoft.ru/"

# url = 'https://test2.minervasoft.ru/login?from=%2F'
# base_url = "https://test2.minervasoft.ru/"
# article_url = "news/space/75?popup=article-editor&chosenSpaceId=75&articleId=new&article-type=ARTICLE"
# url = 'https://test1.minervasoft.ru/login?from=%2F'
# """title"""
# name_project ='selen'
# name_ = 'Весь контент'

#
# text_ru = "С другой стороны курс на социально-ориентированный национальный проект обеспечивает актуальность " \
#           "дальнейших направлений развитая системы массового участия. Соображения высшего порядка, а также " \
#           "дальнейшее развитие различных форм деятельности в значительной степени обуславливает создание " \
#           "существующих финансовых и административных условий?"
#
# text_en = "A lot of the central bank news is priced into equities and investors are now taking a step back" \
#           " to evaluate why central banks have turned more dovish, said David Holohan, a strategist at Mediolanum" \
#           " Asset Management in Dublin."

# Persons 1
"""data input person 1"""
person_1 = "person1"
name_1 = "name1"
mail_1 = "testperson0001@mail.ru"
login_person1 = "login1111"
password_person1 = "97718d75"

# Persons 2
"""data input person 2"""
person_2 = "person1"
name_2 = "name1"
mail_2 = "testperson0001@mail.ru"
login_person2 = "login112"
password_person2 = "63a45e26"

base_article = url + "/content/space/54/article/1938"
article_by_template = url + "/content/space/54/article/1942/page/0"
article_by_script = url + "/content/space/1/folder/89/article/563"