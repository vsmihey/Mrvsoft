import hashlib
import os
import pathlib
import random
import uuid
from itertools import count
from pathlib import Path
import requests
import json
from requests.auth import HTTPBasicAuth
from tempmail import TempMail

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
# lst.reverse()
# print(lst)
# li = sorted(lst, reverse=True)
# print(li)

# url = "https://test6.minervasoft.ru/api/space/55/folder"
# result = requests.get(url, auth=HTTPBasicAuth("m.andrey", 'e70a8e89'))
# resp = result.text
# d = json.loads(resp)
# print(d)



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


#
# tm = TempMail()
# email = tm.get_email_address() # v5gwnrnk7f@gnail.pw
# print(email)
# print(tm.get_mailbox(email))  # list of emails

# from tempmail import TempMail
# tm = TempMail(login='denis', domain='@gnail.pw')
# print(tm.get_mailbox())  # list of emails in denis@gnail.pw



tm = TempMail(api_key='lYTy1Sh54YOW0538l8jNxL4Oc9SHM9P3')

# domains = tm.get_domains()
# print(domains)

# Create a temporary email address with a random username
# email = tm.create_email()
# print(email)


# Create a temporary email address with a specified username

#
# "http://api.temp-mail.org/request/mail/id/md5/"
# email = tm.create_email(username='person1')
# print(email)
#
# email_ = tm.get_mail('mail_id')
# print(email_)




#
# hash_object = hashlib.md5(b'oc5sjMnh@tgvis.com')
# print(hash_object.hexdigest())
#
# url = f"https://api.apilayer.com/temp_mail/mail/id/{hash_object}"
#
# payload = {}
# headers= {
#   "apikey": "lYTy1Sh54YOW0538l8jNxL4Oc9SHM9P3"
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# status_code = response.status_code
# result = response.text
# print(result)

