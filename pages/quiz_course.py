import random
import time

from pages.CKE_redactor_and_public_wizard import PublicWizard
from pages.creating_panel import CreatingPanel
from selenium.webdriver.common.keys import Keys
import locators.all_locators as locators


class Test(CreatingPanel, PublicWizard):
    TEST_STRING = ''.join([str(random.randint(1, 9)) for _ in range(1, 515)])

    def input_test_name(self, text=TEST_STRING):
        """Ввод имени теста"""
        self.element_is_visible(locators.Test.TEST_NAME).send_keys(text)

    def clear_test_name(self):
        """Очистка поля для ввода имени теста"""
        self.element_is_visible(locators.Test.TEST_NAME).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(locators.Test.TEST_NAME).send_keys(Keys.BACKSPACE)

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

    def check_save_button_status_no_active(self):
        """Проверка, что кнопка 'сохранить' не активна """
        assert self.element_is_visible(locators.Test.SAVE_BUTTON).is_enabled() is False

    def check_save_button_status_active(self):
        """Проверка, что кнопка 'сохранить' не активна """
        assert self.element_is_visible(locators.Test.SAVE_BUTTON).is_enabled()

    def add_new_question_button(self):
        """Кнопка добавить новый вопрос"""
        self.click_to_element(locators.Test.NEW_QUESTION_BUTTON)

    def check_name_modal_window(self):
        """Проверка наименования модального окна для добавления вопросов в тест"""
        assert self.element_is_visible(locators.Test.MODAL_WINDOW_NAME).text == 'Выберите вопросы для теста'

    def select_questions(self):
        """Выбор вопросов"""
        self.click_to_element(locators.Test.ALL_QUESTIONS_SELECT)

    def close_modal_window(self):
        """Закрытие модального окна"""
        self.click_to_element(locators.CreateTopicDatabaseLocators.SVG_CLOSE_DELETED_WINDOW)
        time.sleep(1)

    def check_empty_questions_limit(self):
        """Проверка, что вопросы для теста не выбраны"""
        assert self.element_is_visible(
            locators.Test.QUESTIONS_LIMIT_STATUS).text == 'Выберите, сколько случайных вопросов будет в тесте'

    def select_questions_limit(self):
        """Выбор количества вопросов в тесте, по условиям теста 1 вопрос"""
        # self.browser.execute_script("""document.querySelector(".m-ui-slider__input").setAttribute(
        #     'value','22')""") # Если потребуется передавать другое количество вопросов в тест
        self.element_is_visible(locators.Test.QUESTIONS_LIMIT_VALUE).send_keys(Keys.ARROW_RIGHT)

    def check_one_questions_limit(self):
        """Проверка, что в тесте выбран один вопрос"""
        assert self.element_is_visible(
            locators.Test.QUESTIONS_LIMIT_STATUS).text == 'В тесте будет 1 случайный вопрос'

    def save_test(self):
        """Сохранение теста"""
        self.click_to_element(locators.Test.SAVE_BUTTON)
        self.element_is_visible(locators.Test.COUNT_OF_CORRECT_ANSWERS).send_keys('1')
        self.next_and_finish_button_click()
        self.next_and_finish_button_click()
        self.next_and_finish_button_click()


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

    def check_save_button_status_no_active(self):
        """Проверка, что кнопка 'сохранить' не активна """
        assert self.element_is_visible(locators.Quiz.SAVE_BUTTON).is_enabled() is False
