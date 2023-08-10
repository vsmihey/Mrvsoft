from pages.base_class import MainPage
import locators.all_locators as locators


class MenuNavigation(MainPage):
    """Навигация по странице"""

    def history_button_click(self):
        """Переход в историю"""
        self.click_to_element(locators.MenuNavigation.HISTORY_BUTTON)

    def bell_button_click(self):
        """Переход в уведомления (колокольчик)"""
        self.click_to_element(locators.CheckCommentsPersons.BELL_ALERT)
