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

    def create_folder_button(self):
        """Кнопка создания новой папки"""
        self.click_to_element(locators.FormPagesLocators.CREATE_FOLDER_BUTTON)

    def content_button_click(self):
        """Переход в Контент"""
        self.click_to_element(locators.MenuNavigation.CONTENT)

    def learn_button_click(self):
        """Переход в обучение"""
        self.click_to_element(locators.MenuNavigation.LEARN_BUTTON)

    def reports_click(self):
        """Переход в Отчеты"""
        self.click_to_element(locators.FormPagesLocators.REPORT_BUTTON)
