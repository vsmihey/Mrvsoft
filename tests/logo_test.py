import time
from pages.data_login_password import *
from pages.form_page import FormPage



class TestLogo:

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
        # form_page.hover(driver)
        # time.sleep(5)
        # form_page.screenshot()






        # driver.refresh()
        # self.login = 'm.andrey'
        # self.password = '71de90df'
        # form_page.authorization(self.login, self.password)
        # form_page.logo_head()
        # form_page.screenshot()










