from pages.authorisation_page import Authorisation
import locators.all_locators as locators


class CreatingPanel(Authorisation):
    """Класс панели создания статей"""

    def create_button(self):
        """Кнопка для перехода в панель создания статей"""
        self.click_to_element(locators.FormPagesLocators.CREATE_BUTTON)

    def create_base_article_button(self):
        """Кнопка для создания обычной статьи"""
        self.click_to_element(locators.FormPagesLocators.CREATE_ARTICLE)

    def create_sample_article_button(self):
        """Кнопка для создания шаблонной статьи"""
        self.click_to_element(locators.FormPagesLocators.CREATE_ARTICLE)

    def create_stepping_article_button(self):
        """Кнопка для создания пошагового сценария"""
        pass

    def create_test_button(self):
        """Кнопка для создания теста"""
        self.click_to_element(locators.Test.CREATING_TEST_BUTTON)

    def create_course_button(self):
        """Кнопка для создания курса"""
        self.click_to_element(locators.Course.CREATING_COURSE_BUTTON)

    def create_quiz_button(self):
        """Кнопка для создания опроса"""
        self.click_to_element(locators.Quiz.CREATING_QUIZ_BUTTON)

    def task_button(self):
        """Кнопка для назначения задания"""
        self.click_to_element(locators.Task.TASK_BUTTON)

    def draft_button(self):
        """Кнопка черновика"""
        self.click_to_element(locators.FormPagesLocators.DRAFT_BUTTON)

    def education_button_in_draft(self):
        """Кнопка обучения в черновике"""
        self.click_to_element(locators.FormPagesLocators.EDUCATION_BUTTON)


