from pages.authorisation_page import Authorisation
from locators.locators_form_pages import FormPagesLocators
import locators.all_locators as locators


class CreatingPanel(Authorisation):
    """Класс панели создания статей"""

    def create_button(self):
        """Кнопка для перехода в панель создания статей"""
        self.click_to_element(FormPagesLocators.CREATE_BUTTON)

    def create_base_article_button(self):
        """Кнопка для создания обычной статьи"""
        self.click_to_element(FormPagesLocators.CREATE_ARTICLE)

    def create_sample_article_button(self):
        """Кнопка для создания шаблонной статьи"""
        self.click_to_element(FormPagesLocators.CREATE_ARTICLE)

    def create_stepping_article_button(self):
        """Кнопка для создания пошагового сценария"""
        pass

    def create_test_button(self):
        """Кнопка для создания теста"""
        self.click_to_element(locators.Test.CREATING_TEST_BUTTON)

    def create_course_button(self):
        """Кнопка для создания курса"""
        pass

    def create_quiz_button(self):
        """Кнопка для создания опроса"""
        self.click_to_element(locators.Test.CREATING_QUIZ_BUTTON)
