from pages.base_class import MainPage
import locators.all_locators as locators


class MenuNavigation(MainPage):
    """Навигация по странице"""

    def history_button_click(self):
        """Переход в историю"""
        self.element_is_visible(locators.MenuNavigation.HISTORY_BUTTON).click()

    def bell_button_click(self):
        """Переход в уведомления (колокольчик)"""
        self.element_is_visible(locators.CheckCommentsPersons.BELL_ALERT).click()
