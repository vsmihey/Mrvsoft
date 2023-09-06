import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_class import MainPage
from pages.users import person1, person2, person3, person4
from pages.menu_navigation import MenuNavigation
from pages.create_article_and_comments import DataParser
from pages.create_article_and_comments import BaseArticleEditor
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

    def no_empty_history(self) -> str:
        """Метод для проверки, что история не пустая"""
        return self.element_is_invisible(locators.CheckCommentsPersons.EMPTY_HISTORY_CHECK, timeout=1).text

    def status_comment_in_history(self, locator):
        """Проверка, что комментарий в верном статусе"""
        assert self.element_is_visible(locator).is_displayed() is True

    def text_comment_in_history(self, locator, text_comment):
        """Проверка текста комментария"""
        assert self.element_is_visible(locator).text == text_comment

    def history_gray_comment_check(self):
        """Проверка, наличия серого комментария в истории"""
        self.text_comment_in_history(self.GRAY_COMMENT_CHECK, 'Серый комментарий')

    def history_first_solve_comment_check(self):
        """Проверка, наличия 1 ЗАКРЫТОГО комментария в истории"""
        self.status_comment_in_history(self.COMMENT_1_SOLVE_CHECK)
        self.text_comment_in_history(self.COMMENT_1_SOLVE_CHECK, 'Тестовый комментарий 1')

    def history_second_no_solve_comment_check(self):
        """Проверка, наличия 2 НЕ ЗАКРЫТОГО комментария в истории"""
        self.status_comment_in_history(self.COMMENT_2_NO_SOLVE_CHECK)
        self.text_comment_in_history(self.COMMENT_2_NO_SOLVE_CHECK, 'Тестовый комментарий 2')

    def history_second_solve_comment_check(self):
        """Проверка, наличия 2 ЗАКРЫТОГО комментария в истории"""
        self.status_comment_in_history(self.COMMENT_2_SOLVE_CHECK)
        self.text_comment_in_history(self.COMMENT_2_SOLVE_CHECK, 'Тестовый комментарий 2')

    def history_third_no_solve_comment_check(self):
        """Проверка, наличия 3 НЕ ЗАКРЫТОГО комментария в истории"""
        self.status_comment_in_history(self.COMMENT_3_NO_SOLVE_CHECK)
        self.text_comment_in_history(self.COMMENT_3_NO_SOLVE_CHECK, 'Тестовый комментарий 3')

    def history_third_solve_comment_check(self):
        """Проверка, наличия 3 ЗАКРЫТОГО комментария в истории"""
        self.status_comment_in_history(self.COMMENT_3_SOLVE_CHECK)
        self.text_comment_in_history(self.COMMENT_3_SOLVE_CHECK, 'Тестовый комментарий 3')

    def history_four_no_solve_comment_check(self):
        """Проверка, наличия 4 НЕ ЗАКРЫТОГО комментария в истории"""
        self.status_comment_in_history(self.COMMENT_4_NO_SOLVE_CHECK)
        self.text_comment_in_history(self.COMMENT_4_NO_SOLVE_CHECK, 'Тестовый комментарий 4')


class BellAlert(MainPage):
    """Класс для проверки уведомлений (Колокольчик)"""
    BELL_CHECK_TEST_COMMENT_1 = (
        By.XPATH,
        f"//div[text()='{DataParser.get_article_name_from_data_file()}']/../..//div[text()='Тестовый комментарий 1']")
    BELL_CHECK_TEST_COMMENT_2 = (
        By.XPATH,
        f"//div[text()='{DataParser.get_article_name_from_data_file()}']/../..//div[text()='Тестовый комментарий 2']")
    BELL_CHECK_TEST_COMMENT_3 = (
        By.XPATH,
        f"//div[text()='{DataParser.get_article_name_from_data_file()}']/../..//div[text()='Тестовый комментарий 3']")
    BELL_CHECK_TEST_COMMENT_4 = (
        By.XPATH,
        f"//div[text()='{DataParser.get_article_name_from_data_file()}']/../..//div[text()='Тестовый комментарий 4']")
    BELL_CHECK_TEST_COMMENT_GRAY = (
        By.XPATH,
        f"//div[text()='{DataParser.get_article_name_from_data_file()}']/../..//div[text()='Серый комментарий']")
    BELL_CHECK_TEST_CREATE_ARTICLE = (
        By.XPATH,
        f"//div[text()='{DataParser.get_article_name_from_data_file()}']/../..//div[text()='Создание статьи']")
    BELL_CHECK_TEST_MAJOR_EDIT = (
        By.XPATH,
        f"//div[text()='{DataParser.get_article_name_from_data_file()}']/../..//div[text()='Мажорное редактирование']")
    BELL_CHECK_TEST_CLOSE_3 = (By.XPATH, f"//div[text()='{'НАЗВАНИЕ СТАТЬИ'}']/../..//div[text()='Закрытие 3']")

    BELL_CREATE_ARTICLE_CONFIRM = (By.XPATH,
                                   f"//div[text()='подтвердите']/../..//div[text()='{DataParser.get_article_name_from_data_file()}']/../..//div[text()='Создание статьи']")

    def bell_count_notification(self) -> str:
        """Метод для проверки количества непрочитанных уведомлений колокольчика"""
        return self.element_is_visible(locators.CheckCommentsPersons.BELL_ALERT).get_attribute("data-tip")

    def empty_bell(self) -> str:
        """Метод для проверки пустого колокольчика"""
        return self.element_is_visible(locators.CheckCommentsPersons.EMPTY_BELL__CHECK).text

    def text_comment_in_bell(self, locator, text_comment):
        """Проверка текста комментария"""
        assert self.element_is_visible(locator).text == text_comment

    def bell_gray_comment_check(self):
        """Проверка, наличия серого комментария в истории"""
        self.text_comment_in_bell(self.BELL_CHECK_TEST_COMMENT_GRAY, 'Серый комментарий')

    def bell_first_comment_check(self):
        """Проверка, наличия 1 комментария в колокольчике"""
        self.text_comment_in_bell(self.BELL_CHECK_TEST_COMMENT_1, 'Тестовый комментарий 1')

    def bell_second_comment_check(self):
        """Проверка, наличия 2 комментария в колокольчике"""
        self.text_comment_in_bell(self.BELL_CHECK_TEST_COMMENT_2, 'Тестовый комментарий 2')

    def bell_third_comment_check(self):
        """Проверка, наличия 3 комментария в колокольчике"""
        self.text_comment_in_bell(self.BELL_CHECK_TEST_COMMENT_3, 'Тестовый комментарий 3')

    def bell_four_comment_check(self):
        """Проверка, наличия 4 комментария в колокольчике"""
        self.text_comment_in_bell(self.BELL_CHECK_TEST_COMMENT_4, 'Тестовый комментарий 4')

    def check_no_article_notifications_and_history(self):
        """Проверка, что нет записей в истории и уведомлений по конкретной статье по всем статусам"""
        assert self.element_is_invisible(locators.CheckCommentsPersons.CREATE_ARTICLE_CHECK, timeout=0.2)
        assert self.element_is_invisible(locators.CheckCommentsPersons.MAJOR_EDIT_ARTICLE_CHECK, timeout=0.2)
        assert self.element_is_invisible(locators.CheckCommentsPersons.DELETE_ARTICLE_CHECK, timeout=0.2)
        assert self.element_is_invisible(locators.CheckCommentsPersons.RESTORE_ARTICLE_CHECK, timeout=0.2)

    def check_no_article_notifications_and_history_1(self):
        """Проверка, что нет записей в истории и уведомлений по конкретной статье по всем статусам"""
        assert self.element_is_invisible(locators.CheckCommentsPersons.CREATE_ARTICLE_CHECK, timeout=0.2)

    def check_no_article_notifications_and_history_2(self):
        """Проверка, что нет записей в истории и уведомлений по конкретной статье по всем статусам"""
        assert self.element_is_invisible(locators.CheckCommentsPersons.MAJOR_EDIT_ARTICLE_CHECK, timeout=0.2)

    def check_no_article_notifications_and_history_3(self):
        """Проверка, что нет записей в истории и уведомлений по конкретной статье по всем статусам"""
        assert self.element_is_invisible(locators.CheckCommentsPersons.DELETE_ARTICLE_CHECK, timeout=0.2)

    def check_no_article_notifications_and_history_4(self):
        """Проверка, что нет записей в истории и уведомлений по конкретной статье по всем статусам"""
        assert self.element_is_invisible(locators.CheckCommentsPersons.RESTORE_ARTICLE_CHECK, timeout=0.2)

    def check_bell_alert_lms(self, title, text):
        """Проверка колокольчика для курса, теста и опроса. Принимает название и описание колокольчика"""
        self.element_is_visible((By.XPATH, f"//div[text()='{title}']/../..//div[text()='{text}']"), timeout=90)


class PersonValidation(History, BellAlert, MenuNavigation, BaseArticleEditor):
    """Класс проверки функционала пользователями из эталона"""

    def check_open_valid_article(self):
        """Проверка, что открылась нужная статья"""
        assert DataParser.get_article_name_from_data_file() == self.element_is_visible(
            locators.OpenArticle.ARTICLE_TITLE).text

    def check_article_bottom_banner(self):
        """Проверка, что внизу статьи отображается красный банер"""
        assert self.element_is_visible(locators.OpenArticle.CHECK_ARTICLE_BOTTOM_BANNER)

    def check_article_confirm_reading_notification(self):
        """Проверка, что у пользователя отображается банер о подтверждении прочтения уведомления"""
        self.click_to_element(locators.CheckBellComments.BELL_CREATE_ARTICLE_CONFIRM)

    def check_restore_button(self):
        """Проверка, что в удаленной статье внизу есть кнопка 'восстановить'"""
        assert self.element_is_visible(locators.OpenArticle.BOTTOM_BANNER_BUTTON)

    def bottom_banner_button_click(self):
        """Нажатие на кнопку в красном банере внизу статьи"""
        self.click_to_element(locators.OpenArticle.BOTTOM_BANNER_BUTTON)

    def go_to_new_article_from_history_or_bell(self):
        """Проверка перехода в новую статью из истории или колокольчика без подтверждения прочтения"""
        self.click_to_element(locators.CheckCommentsPersons.CREATE_ARTICLE_CHECK)

    def go_to_new_article_from_bell_with_confirm(self):
        """Проверка перехода в новую статью из истории или колокольчика c подтверждением прочтения"""
        self.click_to_element(self.BELL_CREATE_ARTICLE_CONFIRM)

    def go_to_major_edit_article_from_history_or_bell(self):
        """Проверка перехода в статью с мажорным редактированием из истории или колокольчика"""
        self.click_to_element(locators.CheckCommentsPersons.MAJOR_EDIT_ARTICLE_CHECK)

    def go_to_deleted_article_from_history_or_bell(self):
        """Проверка перехода в удаленную статью из истории или колокольчика"""
        self.click_to_element(locators.CheckCommentsPersons.DELETE_ARTICLE_CHECK)

    def go_to_restored_article_from_history_or_bell(self):
        """Проверка перехода в восстановленную статью из истории или колокольчика"""
        self.click_to_element(locators.CheckCommentsPersons.RESTORE_ARTICLE_CHECK)

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
        # self.yes_new_notification()
        self.bell_button_click()

    # def switch_to_learning(self, person):
    #     """Метод переходна на страницу обучения"""

    def close_bell_button(self):
        """Кнопка 'крестик' в колокольчике"""
        self.click_to_element(locators.CheckCommentsPersons.CLOSE_BELL_WINDOW)

    def get_check_bell(self):
        """Метод проверки уведомлений (колокольчик), у каждого пользователя своя реализация метода"""
        pass


class Person1(PersonValidation):
    def switch_to_bell(self, person):
        self.get_authorisation_in_selen(person)
        # try:
        #     self.no_new_notification()
        # except AssertionError:
        #     self.yes_new_notification()
        # finally:
        self.bell_button_click()

    def get_check_history(self):
        self.switch_to_history(person1)

    def get_check_bell(self):
        self.switch_to_bell(person1)


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


class Person4(Person1):

    def get_check_bell(self):
        self.switch_to_bell(person4)
