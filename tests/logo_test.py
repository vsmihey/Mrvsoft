import time
from selenium.common import TimeoutException
from pages.form_page import FormPage
from pages.data_login_password import *

class TestFormPage:

    def test_logo(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.logo_head()
        form_page.screenshot()

        self.login = login
        self.password = password_incorrect
        form_page.authorization(self.login, self.password)
        form_page.restore_incorrect()
        form_page.logo_head()
        form_page.screenshot()

        form_page.full_authorization(driver)
        form_page.logo_head()
        form_page.screenshot()

        form_page.title_find(driver)
        time.sleep(1)