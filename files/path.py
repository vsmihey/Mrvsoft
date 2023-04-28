import os
import pathlib
import uuid
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

sss = os.path.abspath("animal.jpeg")
print(sss)


avatar = Path(pathlib.Path.cwd(), "animal.jpeg")
path = str(avatar)