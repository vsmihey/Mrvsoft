import time
from pages.authorisation_page import Authorisation
from pages.base_class import MainPage
from pages.users import person1, person2, person3, person4
from pages.menu_navigation import MenuNavigation
import locators.all_locators as locators


class History(MainPage):
    """Класс для проверки истории"""

    def empty_history(self) -> str:
        """Метод для проверки пустой истории"""
        return self.element_is_visible(locators.CheckCommentsPersons.EMPTY_HISTORY_CHECK).text


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
        self.yes_new_notification()
        self.bell_button_click()

    def get_check_bell(self):
        """Метод проверки уведомлений (колокольчик), у каждого пользователя своя реализация метода"""
        pass


class Person1(PersonValidation):
    def switch_to_bell(self, person):
        self.get_authorisation_in_selen(person)
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

        time.sleep(5)
