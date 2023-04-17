import time

import pytest
from selenium.common import TimeoutException

from pages import form_page
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


    def test_form_1(self, driver):
        """tests incorrect data"""
        form_page = FormPage(driver, url)
        form_page.open()
        self.login = login_incorrect
        self.password = password
        form_page.fill_fields(self.login, self.password)
        self.login = login_incorrect
        self.password = password_incorrect
        form_page.fill_fields(self.login, self.password)
        self.login = login
        self.password = password_incorrect
        form_page.fill_fields(self.login, self.password)
        form_page.check_auth_text()
        form_page.restore_incorrect()
        form_page.check_restore_text()

    def test_title(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.authorization(login, password)
        form_page.input_project()
        print("input project")
        form_page.all_title(driver)

    @pytest.mark.skip('restore password')
    def test_form_restore(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        password = password_incorrect
        form_page.authorization(login, password)
        form_page.restore_correct()

    def test_add_new_person(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.input_in_my_project(driver)
        form_page.add_new_person(driver)
    def test_add_new_role(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.input_in_my_project(driver)
        form_page.add_new_role(driver)
        time.sleep(1)
















