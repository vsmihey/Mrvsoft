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
def generated_big_file():
    """created bigfile"""
    bf = open('bigfile', "wb")
    bf.seek(1073741824 - 1)
    bf.write(b"\0")
    bf.close()


def generated_file():

    files_list = ["doc", "docx", "odt", "ott", "rtf", "xls", "xlsx", "ods", "ots",
                  "fods", "odp", "otp", "odg", "fodp", "ppt", "pptx", "pdf", "txt", "html", "zip", "jpg", "jpeg", "png", "gif"]
    for i in files_list:
        # path = Path(pathlib.Path.cwd(), "files", f"pic{random.randint(1, 99)}.{i}")
        path = Path(f"pic{random.randint(1, 99)}.{i}")
        # path = os.path.abspath(f"pic{random.randint(1, 99)}.jpg")
        file = open(path, "w+")
        file.close()
        print(file.name)
        # return file.name, path

    # # path = Path(pathlib.Path.cwd(), "files", f"pic{random.randint(1, 99)}.{i}")
    # path = Path(f"pic{random.randint(1, 99)}.xls")
    # # path = os.path.abspath(f"pic{random.randint(1, 99)}.jpg")
    # file = open(path, "w+")
    # file.close()
    # print(file.name)
    # return file.name, path