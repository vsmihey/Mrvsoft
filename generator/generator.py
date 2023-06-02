import os
import pathlib
import random
from pathlib import Path

from data.data import Person
from faker import Faker
faker_en = Faker('En')


def generated_person():
    return Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        mobile=faker_en.msisdn(),
        subject='English'
    )

def generated_file():
    bf = open('newfile', "wb")
    bf.seek(1073741824 - 1)
    bf.write(b"\0")
    bf.close()
    # os.stat("newfile").st_size


    files_list = ["jpg", "jpeg", "png", "gif"]
    for i in files_list:
        # path = Path(pathlib.Path.cwd(), "files", f"pic{random.randint(1, 99)}.{i}")
        path = Path(f"pic{random.randint(1, 99)}.{i}")
        # path = os.path.abspath(f"pic{random.randint(1, 99)}.jpg")
        file = open(path, "w+")
        file.close()
        print(file.name)
        # return file.name, path