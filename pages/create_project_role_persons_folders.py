import time
import random
from locators import all_locators as locators
from pages.authorisation_page import Authorisation
from pages.menu_navigation import MenuNavigation
from pages.base_class import MainPage
from selenium.webdriver.common.by import By


class Folders(MainPage):
    """Класс для работы с папками"""

    pass


class NewProject(Authorisation, MenuNavigation):
    """Класс для создания нового проекта в системе"""
    PROJECT_NAME = 'Название проекта ' + str(random.randint(999, 9999))
    TEST_PROJECT = (By.XPATH,
                    f"//div[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x20 m-space-list-item__title'][normalize-space()='{PROJECT_NAME}']")

    def add_new_project_button(self):
        """Кнопка создания нового проекта"""
        self.click_to_element(locators.FormPagesLocators.ADD)

    def input_project_name(self, name=PROJECT_NAME):
        """Ввод названия проекта"""
        self.element_is_visible(locators.FormPagesLocators.ADD_NAMES_PROJECT).send_keys(name)

    def input_project_description(self, description='test_selenium'):
        """Ввод описания проекта"""
        self.element_is_visible(locators.FormPagesLocators.ADD_DESCRIPTION_PROJECT).send_keys(description)

    def finish_add_new_project_button(self):
        """Кнопка подтверждения создания нового проекта, нажимается после заполнения всех полей"""
        self.click_to_element(locators.FormPagesLocators.ADD_PROJECT_BUTTON)

    def selecting_new_project_to_enter(self):
        """Выбор нового проекта для входа"""
        self.click_to_element(self.TEST_PROJECT)

    def check_project_name(self):
        """Проверка, что вход осуществился в нужный проект"""
        # TODO: написать метод проверки авторизации в нужный проект
        pass

    def creating_new_project(self):
        """Создание нового проекта"""
        self.get_authorisation_no_project_selection()
        self.add_new_project_button()
        self.input_project_name()
        self.input_project_description('Тестовое описание')
        self.finish_add_new_project_button()
