import os
import pathlib
import random
import uuid
from itertools import count
from pathlib import Path

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

# sss = os.path.abspath("animal.jpeg")
# print(sss)


avatar = Path(pathlib.Path.cwd(), "media.jpeg")
path = str(avatar)

print(path)


a="dfgg"+str(random.randint(99,999))
d = random.randint(99, 999)
print(a)
print(type(d))


from random import choice
from string import ascii_uppercase

# для цифр заменить ascii_uppercase на digits
ddd = ''.join(choice(ascii_uppercase) for i in range(256))+str(7)
print(ddd)
print(len(ddd))
