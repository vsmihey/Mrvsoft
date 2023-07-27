import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from pages.authorisation_page import Authorisation
from pages.base_class import MainPage
from pages.users import person1, person2, person3, person4
from pages.menu_navigation import MenuNavigation
from pages.create_article_and_comments import DataParser
import locators.all_locators as locators


class History(MainPage):
    """Класс для проверки истории"""
    COMMENT_1_SOLVE_CHECK = (By.XPATH,
                             f"//h3[text()='{DataParser.get_article_name_from_data_file()}']/../../div[text()='решено']/../..//pre[text()='Тестовый комментарий 1']")
    COMMENT_2_NO_SOLVE_CHECK = (By.XPATH,
                                f"//h3[text()='{DataParser.get_article_name_from_data_file()}']/../../div[text()='не решено']/../..//pre[text()='Тестовый комментарий 2']")
    COMMENT_2_SOLVE_CHECK = (By.XPATH,
                             f"//h3[text()='{DataParser.get_article_name_from_data_file()}']/../../div[text()='решено']/../..//pre[text()='Тестовый комментарий 2']")

    COMMENT_3_NO_SOLVE_CHECK = (By.XPATH,
                                f"//h3[text()='{DataParser.get_article_name_from_data_file()}']/../../div[text()='не решено']/../..//pre[text()='Тестовый комментарий 3']")
    COMMENT_3_SOLVE_CHECK = (By.XPATH,
                             f"//h3[text()='{DataParser.get_article_name_from_data_file()}']/../../div[text()='решено']/../..//pre[text()='Тестовый комментарий 3']")

    COMMENT_4_NO_SOLVE_CHECK = (By.XPATH,
                                f"//h3[text()='{DataParser.get_article_name_from_data_file()}']/../../div[text()='не решено']/../..//pre[text()='Тестовый комментарий 4']")
    GRAY_COMMENT_CHECK = (By.XPATH, "(//pre[contains(text(),'Серый комментарий')])[1]")

    def empty_history(self) -> str:
        """Метод для проверки пустой истории"""
        return self.element_is_visible(locators.CheckCommentsPersons.EMPTY_HISTORY_CHECK).text

    def status_comment_in_history(self, locator):
        """Проверка, что комментарий в верном статусе"""
        assert locator.is_displayed() is True

    def text_comment_in_history(self, locator, text_comment):
        """Проверка текста комментария"""
        assert self.element_is_visible(locator).text == text_comment

    def go_to_new_article_from_history(self):
        """Проверка перехода в новую статью из истории"""
        self.element_is_visible(locators.CheckCommentsPersons.CREATE_ARTICLE_CHECK).click()

    def go_to_minor_edit_article_from_history(self):
        """Проверка перехода в статью с минорным редактированием из истории"""
        self.element_is_visible(locators.CheckCommentsPersons.MINOR_EDIT_ARTICLE_CHECK).click()

    def go_to_major_edit_article_from_history(self):
        """Проверка перехода в статью с мажорным редактированием из истории"""
        self.element_is_visible(locators.CheckCommentsPersons.MAJOR_EDIT_ARTICLE_CHECK).click()

    def check_open_valid_article(self):
        """Проверка, что из истории открылась нужная статья"""
        assert DataParser.get_article_name_from_data_file() == self.element_is_visible(
            locators.OpenArticle.ARTICLE_TITLE).text

    # def new_article_history_check(self):
    #     """Проверка, комментов в истории по новой статье"""
    #     time.sleep(1)
    #     self.text_comment_in_history(self.GRAY_COMMENT_CHECK, 'Серый комментарий')
    #     # print(self.element_is_visible(self.COMMENT_4_NO_SOLVE_CHECK).is_displayed())
    #     # print(self.browser.find_element(*self.COMMENT_4_NO_SOLVE_CHECK).is_displayed())
    #     self.status_comment_in_history(self.browser.find_element(*self.COMMENT_4_NO_SOLVE_CHECK))
    #     # self.browser.find_element(*self.COMMENT_4_NO_SOLVE_CHECK).is_displayed() is True
    #     self.text_comment_in_history(self.COMMENT_4_NO_SOLVE_CHECK, 'Тестовый комментарий 4')
    #     # # print(self.element_is_visible(self.COMMENT_3_NO_SOLVE_CHECK).is_displayed())
    #     # self.status_comment_in_history(*self.COMMENT_3_NO_SOLVE_CHECK)
    #     self.status_comment_in_history(self.browser.find_element(*self.COMMENT_3_NO_SOLVE_CHECK))
    #     self.text_comment_in_history(self.COMMENT_3_NO_SOLVE_CHECK, 'Тестовый комментарий 3')
    #     # # # print(self.element_is_visible(self.COMMENT_2_NO_SOLVE_CHECK).is_displayed())
    #     # self.status_comment_in_history(*self.COMMENT_2_NO_SOLVE_CHECK)
    #     self.status_comment_in_history(self.browser.find_element(*self.COMMENT_2_NO_SOLVE_CHECK))
    #     self.text_comment_in_history(self.COMMENT_2_NO_SOLVE_CHECK, 'Тестовый комментарий 2')
    #     # # # print(self.element_is_visible(self.COMMENT_1_SOLVE_CHECK).is_displayed())
    #     # # print(self.element_is_visible(self.COMMENT_1_SOLVE_CHECK).is_displayed())
    #     self.status_comment_in_history(self.browser.find_element(*self.COMMENT_1_SOLVE_CHECK))
    #     # # self.status_comment_in_history(self.COMMENT_1_SOLVE_CHECK)
    #     self.text_comment_in_history(self.COMMENT_1_SOLVE_CHECK, 'Тестовый комментарий 1')

    def new_article_history_check(self):
        """Проверка, комментов в истории по новой статье"""
        self.text_comment_in_history(self.GRAY_COMMENT_CHECK, 'Серый комментарий')
        self.status_comment_in_history(self.browser.find_element(*self.COMMENT_1_SOLVE_CHECK))
        self.text_comment_in_history(self.COMMENT_1_SOLVE_CHECK, 'Тестовый комментарий 1')

    def minor_edit_article_history_check(self):
        """Проверка, комментов в истории по минорному редактированию статье"""
        self.status_comment_in_history(self.browser.find_element(*self.COMMENT_2_SOLVE_CHECK))
        self.text_comment_in_history(self.COMMENT_2_SOLVE_CHECK, 'Тестовый комментарий 2')

    def major_edit_article_history_check(self):
        """Проверка, комментов в истории по мажорному редактированию статье"""
        self.status_comment_in_history(self.browser.find_element(*self.COMMENT_3_SOLVE_CHECK))
        self.text_comment_in_history(self.COMMENT_3_SOLVE_CHECK, 'Тестовый комментарий 3')


class BellAlert(MainPage):
    """Класс для проверки уведомлений (Колокольчик)"""

    def bell_count_notification(self) -> str:
        """Метод для проверки количества непрочитанных уведомлений колокольчика"""
        return self.element_is_visible(locators.CheckCommentsPersons.BELL_ALERT).get_attribute("data-tip")

    def empty_bell(self) -> str:
        """Метод для проверки пустого колокольчика"""
        return self.element_is_visible(locators.CheckCommentsPersons.EMPTY_BELL__CHECK).text


class PersonValidation(Authorisation, History, BellAlert, MenuNavigation):
    """Класс проверки функционала пользователями из эталона"""

    def empty_history_check(self):
        """Проверка, что в истории пусто"""
        assert self.empty_history() == 'Пока в этом проекте ничего не происходило'

    def empty_bell_check(self):
        """Метод проверки, что при нажатии на колокольчик внутри нет уведомлений"""
        assert self.empty_bell() == 'Нет непрочитанных уведомлений'

    def no_new_notification(self):
        """Метод проверки, что нет новых уведомлений (красные цифры на колокольчике)"""
        assert self.bell_count_notification() == 'нет уведомлений'

    def yes_new_notification(self):
        """Метод проверки, что есть новые уведомления (красные цифры на колокольчике)"""
        assert self.bell_count_notification() != 'нет уведомлений'

    def switch_to_history(self, person):
        """Метод переходна на страницу истории, с прохождением авторизации"""
        self.get_authorisation_in_selen(person)
        self.history_button_click()

    def get_check_history(self):
        """Метод проверки истории, у каждого пользователя своя реализация метода"""
        pass

    def switch_to_bell(self, person):
        """Метод переходна на страницу истории, с прохождением авторизации"""
        self.get_authorisation_in_selen(person)
        time.sleep(1)
        self.yes_new_notification()
        self.bell_button_click()

    def get_check_bell(self):
        """Метод проверки уведомлений (колокольчик), у каждого пользователя своя реализация метода"""
        pass


class Person1(PersonValidation):
    def switch_to_bell(self, person):
        self.get_authorisation_in_selen(person)
        time.sleep(1)
        self.no_new_notification()
        self.bell_button_click()

    def get_check_history(self):
        self.switch_to_history(person1)
        self.empty_history_check()

    def get_check_bell(self):
        self.switch_to_bell(person1)
        self.empty_bell_check()


class Person2(PersonValidation):

    def get_check_history(self):
        self.switch_to_history(person2)

    def get_check_bell(self):
        self.switch_to_bell(person2)


class Person3(PersonValidation):

    def get_check_history(self):
        self.switch_to_history(person3)

    def get_check_bell(self):
        self.switch_to_bell(person3)


class Person4(PersonValidation):

    def get_check_history(self):
        self.switch_to_history(person4)

    def get_check_bell(self):
        self.switch_to_bell(person4)
