import time
import pytest
from pages.files_format_page import FilesFormatPage
from pages.data_login_password import *


class TestFilesFormat:

    class TestCheckFormat:

        def test_add_support_files(self, driver):
            files_format_page = FilesFormatPage(driver, url)
            files_format_page.open()
            files_format_page.add_files_pict(driver)







