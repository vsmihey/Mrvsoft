import time
import pytest
from pages.files_format_page import FilesFormatPage
from pages.data_login_password import *


class TestFilesFormat:

    class TestCheckFormat:

        def test_add_pic_files(self, driver):
            files_format_page = FilesFormatPage(driver, url)
            files_format_page.open()
            files_format_page.add_files_pict(driver)

        def test_audio_files(self, driver):
            files_format_page = FilesFormatPage(driver, url)
            files_format_page.open()
            files_format_page.check_audio_files(driver)

        def test_video_files(self, driver):
            files_format_page = FilesFormatPage(driver, url)
            files_format_page.open()
            files_format_page.check_video_files(driver)

        # def test_file_replacement(self, driver):
        #     files_format_page = FilesFormatPage(driver, url)
        #     files_format_page.open()










