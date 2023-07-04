import os
import pathlib
import random
from pathlib import Path
from data.data import Person
from faker import Faker
from tempmail import TempMail


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
    files_list = ["csv", "exe", "odt", "ott", "rtf", "ots",
                  "fods", "odp", "otp", "odg", "fodp", "ppt", "pptx"]
    # files_list = ["html", "jpg", "jpeg", "png", "gif"]
    data_files = []
    for i in files_list:
        # path = Path(pathlib.Path.cwd(), "files", f"pic{random.randint(1, 99)}.{i}")
        path = Path(f"file{random.randint(1, 99)}.{i}")
        # path = os.path.abspath(f"pic{random.randint(1, 99)}.jpg")
        file = open(path, "w+")
        file.close()
        # print(file.name)
        data_files.append(path)
        # return file.name, path
    return data_files


def generated_files_audio():
    audio_files_format = ["ac3", "aiff", "au", "dts", "flac", "m4a", "m4p", "m4r", "mp2", "ogg", "opus", "ra", "tta", "voc", "vox", "wav", "wma"]
    audio_files = []
    for i in audio_files_format:
        path = Path(f"file{random.randint(1, 99)}.{i}")
        file = open(path, "w+")
        file.close()
        audio_files.append(path)
    return audio_files


def generated_files_video():
    video_files_format = ["flv", "mov", "3gp", "m4v", "asf", "m2ts", "m4v", "mkv", "mts", "swf", "vob", "wmv", "webm"]
    video_files = []
    for i in video_files_format:
        path = Path(f"file{random.randint(1, 99)}.{i}")
        file = open(path, "w+")
        file.close()
        video_files.append(path)
    return video_files

# def temp_mail():
#     tm = TempMail()
#     email = tm.get_email_address()  # v5gwnrnk7f@gnail.pw
#     print(tm.get_mailbox(email))  # list of emails