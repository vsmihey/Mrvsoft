import time
import pytest
from pages.files_format_page import FilesFormatPage, UnformatFilePage
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

        def test_create_pic_video_audio_files(self, driver):
            files_format_page = FilesFormatPage(driver, url)
            files_format_page.open()
            files_format_page.create_pic_video_audio_files(driver)

        def test_file_check_replacement_video(self, driver):
            files_format_page = FilesFormatPage(driver, url)
            files_format_page.open()
            files_format_page.check_replacement_files_video(driver)

        def test_file_check_replacement_audio(self, driver):
            files_format_page = FilesFormatPage(driver, url)
            files_format_page.open()
            files_format_page.file_check_replacement_audio(driver)

        def test_file_check_replacement_pic(self, driver):
            files_format_page = FilesFormatPage(driver, url)
            files_format_page.open()
            files_format_page.file_check_replacement_pic(driver)

    class TestUnformatFile:

        def test_add_unformat_file(self, driver):
            files_format_page = UnformatFilePage(driver, url)
            files_format_page.open()
            files_format_page.add_unformat_file_rar_zip(driver)
            files_format_page.add_unformat_file_exel()
            files_format_page.add_unformat_file_other()













