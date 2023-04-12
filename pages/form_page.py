import datetime
import time
from selenium.webdriver import ActionChains, Keys
from pages.base_page import BasePage
from locators.form_pages_locators import FormPagesLocators as Locators
from pages.data_login_password import *

class FormPage(BasePage):

    def full_authorization(self, driver):
        """correct data"""
        self.login = login
        self.password = password
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.authorization(self.login, self.password)
        # form_page.check_project_page()
        # time.sleep(1)

    def authorization(self, login, password):
        self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.INPUT_BUTTON).click()
        time.sleep(1)

    def fill_fields(self, login, password):
        self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.INPUT_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(Locators.LOGIN).clear()
        self.element_is_visible(Locators.PASSWORD).clear()
        time.sleep(1)

    def check_auth_text(self):
        check_logit_text = self.element_is_visible(Locators.INCORRECT_LOGIN_TEXT)
        check_logit_text_value = check_logit_text.text
        assert check_logit_text_value == 'Неверный логин'
        check_password_text = self.element_is_visible(Locators.INCORRECT_PASSWORD_TEXT)
        check_password_text_value = check_password_text.text
        assert check_password_text_value == 'Неверный пароль'
        print('Ткст авторизации: ' + check_logit_text_value, check_password_text_value + ' УСПЕШНО')

    def restore_incorrect(self):
        login = login_incorrect
        self.element_is_visible(Locators.RESTORE).click()
        self.element_is_visible(Locators.RESTORE_LOGIN).send_keys(login)
        self.element_is_visible(Locators.RESTORE_BUTTON).click()
        # self.element_is_visible(Locators.REMEMBER_PASSWD)

    def check_restore_text(self):
        check_logit_text = self.element_is_visible(Locators.INCORRECT_LOGIN_TEXT)
        check_logit_text_value = check_logit_text.text
        assert check_logit_text_value == 'Неверный логин'
        print('Текст восстановления: ' + check_logit_text_value + ' УСПЕШНО')

    def restore_correct(self):
        login
        self.element_is_visible(Locators.RESTORE_LOGIN).send_keys(login)
        self.element_is_visible(Locators.RESTORE_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(Locators.RESTORE_BUTTON).click()
        self.element_is_visible(Locators.REMEMBER_PASSWD).click()
        print('Письмо с новым паролем отправлено на почту УСПЕШНО')

    def screenshot(self):
        offset = datetime.timezone(datetime.timedelta(hours=3))  # timezone (+3)
        now_date = datetime.datetime.now(offset)
        now_date = now_date.strftime('%Y.%m.%d.%H.%M.%S')
        # now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot.png' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\User\\PycharmProjects\\Minervasoft\\screen\\' + name_screenshot)

    def check_project_page(self):
        check_project = self.element_is_visible(Locators.CHANGE_PROJECT)
        check_project_value = check_project.text
        assert check_project_value == 'Выберите проект'
        print('Страница ' + check_project_value + ' открыта')

    def logo_head(self):
        """LOGO"""
        logo = self.element_is_visible(Locators.LOGO_HEAD)
        print(logo.is_displayed())

    def hover(self, driver):
        """MOUSE"""
        element = self.element_is_visible(Locators.LOGO_HEAD)
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()

    def input_project(self, driver):
        self.element_is_visible(Locators.TEST_PROJECT).click()
        action = ActionChains(self, driver)
        action.send_keys(Keys.TAB)
        action.send_keys(Keys.TAB)
        time.sleep(30)
        # self.element_is_visible(Locators.TAB)
        # self.element_is_visible(Locators.TAB)
        # self.element_is_visible(Locators.ENTER)

        time.sleep(5)

