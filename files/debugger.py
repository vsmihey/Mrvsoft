import os
import pathlib
import random
import uuid
from itertools import count
from pathlib import Path
import requests
import json
from requests.auth import HTTPBasicAuth

# home = Path.home()
# wave_absolute = Path("files", "animal.jpeg")
# # print(home)
# print(wave_absolute)

# path = Path(pathlib.Path.cwd(), "animal.jpeg")
# print(str(path))

# dddd = os.getcwd()
# print(dddd)
#
# path = Path("animal.jpeg")
# path = str(path)
# print(path)
#
# path = Path(pathlib.Path.cwd(), "files" ,"animal.jpeg")
# print(str(path))
#
# wave_absolute = Path("files", "animal.jpeg")
# print(wave_absolute)



# filename = Path(pathlib.Path.home(), "files", "animal.jpeg")
# # filename.open()
# print(str(filename))
#
# ddd = pathlib.Path.cwd() / 'Minervasoft' / 'files' / 'animal.jpeg'
# # Выводит "source_data\text_files\raw_data.txt" на Windows
#
# print(ddd)

sss = os.path.abspath("gomer.gif")
print(sss)

# data_unsupported = ["w", "e"]
# i = random.randint(0, 1)
# data_unsupported = data_unsupported[i]
# print(data_unsupported, type(data_unsupported))

# рандомно выбрать несколько элементов из списка
# lst = [10, 25, 30, 45, 50 ,65, 70, 85, 90, 105]
# list_random = random.choices(lst, k=3)
# print(list_random)
#
#
# lst = [10, 25, 30, 45, 50 ,65, 70, 85, 90, 105]
#
# li = sorted(lst, reverse=True)
# print(li)

url = "https://test6.minervasoft.ru/api/space/55/folder"
result = requests.get(url, auth=HTTPBasicAuth("m.andrey", 'e70a8e89'))
resp = result.text
d = json.loads(resp)
print(d)



# avatar = Path(pathlib.Path.cwd(), "media.jpeg")
# path = str(avatar)
#
# print(path)
#
#
# a="dfgg"+str(random.randint(99,999))
# d = random.randint(99, 999)
# print(a)
# print(type(d))
#
# from random import choice
# from string import ascii_uppercase
#
# # для цифр заменить ascii_uppercase на digits
# ddd = ''.join(choice(ascii_uppercase) for i in range(256))+str(7)
# print(ddd)
# print(len(ddd))
#
# text_content = "OpenAI is GPT-3 model is an impressive language model that has gained significant attention. " \
#                     " It has been trained on a massive amount of data and can generate human-like text in a wide range " \
#                     "of topics and styles. You can learn more about GPT-3 by visiting the https://openai.com/ and exploring their documentation and resources. " \
#                     "Feel free to click on the link to delve into the fascinating world of GPT-3 and discover its capabilities!"
#
# print(len(text_content))


# универальный путь
# s = '/foo/bar/zoo/file.ext'
# import ntpath
# import os
# s.replace(os.sep,ntpath.sep)
# '\\foo\\bar\\zoo\\file.ext'


