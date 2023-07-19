import time
from pages import data_login_password
from pages import users
import locators.all_locators as locators
from pages.base_class import MainPage


class Authorisation(MainPage):
    """Класс авторизации в системе"""

    def select_authorisation_type(self):
        """Выбирается "встроенный" тип авторизации"""
        self.element_is_visible(locators.AuthorisationPage.TYPE_AUTHOR).send_keys('Встроенный')

    def input_login(self, login=data_login_password.login):
        """Заполняем поле для ввода логина, если не передаем логин, по дефолту вводит логин админа"""
        self.element_is_visible(locators.AuthorisationPage.LOGIN).send_keys(login)

    def input_password(self, password=data_login_password.password):
        """Заполняем поле для ввода пароля, если не передаем пароль, по дефолту вводит пароль админа"""
        self.element_is_visible(locators.AuthorisationPage.PASSWORD).send_keys(password)

    def confirm_button(self):
        """Нажимаем кнопку войти"""
        self.element_is_visible(locators.AuthorisationPage.INPUT_BUTTON).click()

    def select_project_superbank(self):
        """Выбор проекта СуперБанка"""
        self.element_is_visible(locators.AuthorisationPage.SUPER_BANK_PROJECT).click()

    def select_project_selen(self):
        """Выбор проекта Selen"""
        self.element_is_visible(locators.AuthorisationPage.TEST_PROJECT).click()

    def checking_the_authorization_page(self) -> str:
        """Проверка, что открыта страница авторизации"""
        return self.element_is_visible(locators.AuthorisationPage.INPUT_IN_SYSTEM_TEXT).text

    def get_authorisation_in_superbank(self, user=users.admin):
        """Метод для прохождения авторизации в проект СуперБанка"""
        self.open()
        self.select_authorisation_type()
        self.input_login(user.login)
        self.input_password(user.password)
        self.confirm_button()
        self.select_project_superbank()

    def get_authorisation_in_selen(self, user=users.admin):
        """Метод для прохождения авторизации в проект Selen"""
        self.open()
        self.select_authorisation_type()
        self.input_login(user.login)
        self.input_password(user.password)
        self.confirm_button()
        self.select_project_selen()

    def get_authorisation_in_url(self, url, user=users.admin):
        """Метод для прохождения авторизации и перехода по переданной ссылке"""
        self.open(url=url)
        self.select_authorisation_type()
        self.input_login(user.login)
        self.input_password(user.password)
        self.confirm_button()

