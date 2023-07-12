import time
import base_class
import data_login_password
from selenium.webdriver.common.by import By
from locators.locators_form_pages import FormPagesLocators

class Authorisation(base_class.MainPage):
    '''Класс авторизации в системе'''

    def select_authorisation_type(self):
        '''Выбирается "встроенный" тип авторизации'''
        self.browser.find_element(*FormPagesLocators.TYPE_AUTHOR).send_keys('Встроенный')


    def input_login(self, login = data_login_password.user_login_pogodin):
        '''Заполняем поле для ввода логина, если не передаем логин по дефолту вводит логин админа'''
        self.browser.find_element(*FormPagesLocators.LOGIN).send_keys(login)

    def input_password(self, password = data_login_password.user_password_pogodin):
        '''Заполняем поле для ввода пароля, если не передаем пароль по дефолту вводит пароль админа'''
        self.browser.find_element(*FormPagesLocators.PASSWORD).send_keys(password)

    def confirm_button(self):
        '''Нажимаем кнопку войти'''
        self.browser.find_element(*FormPagesLocators.INPUT_BUTTON).click()

    def select_project(self):
        '''Выбор проекта СуперБанка'''
        self.browser.find_element(*FormPagesLocators.SUPER_BANK_PROJECT).click()

    @staticmethod
    def get_authorisation():
        '''Авторизация'''
        try:
            page = Authorisation()
            page.open()
            page.select_authorisation_type()
            page.input_login()
            page.input_password()
            page.confirm_button()
            page.select_project()
            time.sleep(10)
            assert page.get_actual_url() == f'{data_login_password.url}/news/space/1'
            print('Авторизация - Passed')
        except:
            print('Авторизация - Failed')


if __name__ == '__main__':
    Authorisation.get_authorisation()
    base_class.driver.quit()
