import time
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


    def test_form_1(self, driver):
        """incorrect data"""

        self.login = login_incorrect
        self.password = password
        form_page = FormPage(driver, url)
        form_page.open()
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
        form_page.restore_correct()
        time.sleep(1)
        form_page.screenshot()

    def test_title(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.full_authorization(driver)
        form_page.input_project(driver)













    # def test_authorization(self, driver):
    #     """correct data"""
    #     self.login = 'm.andrey'
    #     self.password = '46bf6f4f'
    #     form_page = FormPage(driver, 'https://test1.minervasoft.ru/login?from=%2F')
    #     form_page.open()
    #     form_page.authorization(self.login, self.password)
    #     form_page.check_project_page()
    #     time.sleep(1)
    #     print()



    # def form_restore(self, driver):
    #     pass
        # self.login = 'm.andre'
        # self.password = '753f9f5a'
        # form_page = FormPage(driver, 'https://test1.minervasoft.ru/login?from=%2F')
        # form_page.open()
        # form_page.fill_fields_negative(self.login, self.password)
        # form_page.restore_incorrect()
        # time.sleep(2)
        # form_page.check_restore_text()
        # time.sleep(2)
        # form_page.restore_correct()
        # time.sleep(2)













