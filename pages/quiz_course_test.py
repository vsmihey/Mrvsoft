import random
from pages.creating_panel import CreatingPanel
import locators.all_locators as locators


class Test(CreatingPanel):
    TEST_STRING = ''.join([str(random.randint(1, 9)) for _ in range(1, 515)])

    def input_test_name(self):
        """Ввод имени теста"""
        self.element_is_visible(locators.Test.TEST_NAME).send_keys(self.TEST_STRING)

    def check_test_name_length(self):
        """ Метод проверки корректности названия теста, длина не должна превышать 128 символов, название должно
        соответствовать первым 128 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Test.TEST_NAME).get_attribute('value'))) == 128
        assert self.element_is_visible(locators.Test.TEST_NAME).get_attribute('value') == self.TEST_STRING[:128]

    def input_test_description(self):
        """Ввод описания теста"""
        self.element_is_visible(locators.Test.TEST_DESCRIPTION).send_keys(self.TEST_STRING)

    def check_test_description_length(self):
        """ Метод проверки корректности описания теста, длина не должна превышать 512 символов, название должно
        соответствовать первым 512 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Test.TEST_DESCRIPTION).get_attribute('value'))) == 512
        assert self.element_is_visible(locators.Test.TEST_DESCRIPTION).get_attribute('value') == self.TEST_STRING[:512]

    def check_save_button_status(self):
        """Проверка, что кнопка 'сохранить' не активна """
        assert self.element_is_visible(locators.Test.SAVE_BUTTON).is_enabled() is False

    def add_new_question_button(self):
        """Кнопка добавить новый вопрос"""
        self.click_to_element(locators.Test.NEW_QUESTION_BUTTON)

    def check_name_model_window(self):
        """Проверка наименования модального окна для добавления вопросов в тест"""
        assert self.element_is_visible(locators.Test.MODAL_WINDOW_NAME).text == 'Выберите вопросы для теста'

    def select_questions(self):
        """Выбор вопросов"""
        self.click_to_element(locators.Test.ALL_QUESTIONS_SELECT)


class Quiz(Test):
    def input_quiz_name(self):
        """Ввод имени опроса"""
        self.element_is_visible(locators.Quiz.QUIZ_NAME).send_keys(self.TEST_STRING)

    def check_quiz_name_length(self):
        """ Метод проверки корректности названия опроса, длина не должна превышать 128 символов, название должно
        соответствовать первым 128 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Quiz.QUIZ_NAME).get_attribute('value'))) == 128
        assert self.element_is_visible(locators.Quiz.QUIZ_NAME).get_attribute('value') == self.TEST_STRING[:128]

    def input_quiz_description(self):
        """Ввод описания опроса"""
        self.element_is_visible(locators.Quiz.QUIZ_DESCRIPTION).send_keys(self.TEST_STRING)

    def check_quiz_description_length(self):
        """ Метод проверки корректности описания опроса, длина не должна превышать 128 символов, название должно
        соответствовать первым 512 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Quiz.QUIZ_DESCRIPTION).get_attribute('value'))) == 128
        assert self.element_is_visible(locators.Quiz.QUIZ_DESCRIPTION).get_attribute('value') == self.TEST_STRING[:128]

    def check_save_button_status(self):
        """Проверка, что кнопка 'сохранить' не активна """
        assert self.element_is_visible(locators.Quiz.SAVE_BUTTON).is_enabled() is False
