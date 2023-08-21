import random
import time

from pages.CKE_redactor_and_public_wizard import PublicWizard, CKERedactor
from pages.creating_panel import CreatingPanel
from selenium.webdriver.common.keys import Keys
from locators.all_locators import CreateTopicDatabaseLocators as locators_topic_database

import locators.all_locators as locators


class UUU(CreatingPanel, PublicWizard, CKERedactor):
    TEST_STRING = ''.join([str(random.randint(1, 9)) for _ in range(1, 515)])
    TITLE = 'Название теста ' + str(random.randint(99, 9999))

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
        """Проверка, что кнопка 'сохранить' активна """
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

    def check_name_created_test(self):
        """Проверка, карточки созданного теста по совпадению названия теста"""
        assert self.element_is_visible(locators.Test.NAME_CREATED_TEST).text == self.TITLE


class Quiz(Test):
    TEST_STRING = Test.TEST_STRING
    TITLE = Test.TITLE

    def input_quiz_name(self, text=TEST_STRING):
        """Ввод имени опроса"""
        self.element_is_visible(locators.Quiz.QUIZ_NAME).send_keys(text)

    def clear_quiz_name(self):
        """Очистка поля для ввода имени теста"""
        self.element_is_visible(locators.Quiz.QUIZ_NAME).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(locators.Quiz.QUIZ_NAME).send_keys(Keys.BACKSPACE)

    def check_quiz_name_length(self):
        """ Метод проверки корректности названия опроса, длина не должна превышать 128 символов, название должно
        соответствовать первым 128 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Quiz.QUIZ_NAME).get_attribute('value'))) == 128
        assert self.element_is_visible(locators.Quiz.QUIZ_NAME).get_attribute('value') == self.TEST_STRING[:128]

    def input_quiz_description(self):
        """Ввод описания опроса"""
        self.element_is_visible(locators.Quiz.QUIZ_DESCRIPTION).send_keys(self.TEST_STRING)

    def check_quiz_description_length(self):
        """ Метод проверки корректности описания опроса, длина не должна превышать 128 символов, описание должно
        соответствовать первым 128 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Quiz.QUIZ_DESCRIPTION).get_attribute('value'))) == 128
        assert self.element_is_visible(locators.Quiz.QUIZ_DESCRIPTION).get_attribute('value') == self.TEST_STRING[:128]

    def check_save_button_status_no_active(self):
        """Проверка, что кнопка 'сохранить' не активна """
        assert self.element_is_visible(locators.Quiz.SAVE_BUTTON).is_enabled() is False

    def check_save_button_status_active(self):
        """Проверка, что кнопка 'сохранить' активна """
        assert self.element_is_clickable(locators.Quiz.SAVE_BUTTON)

    def add_new_question_button(self):
        """Кнопка добавить новый вопрос"""
        self.click_to_element(locators.Quiz.NEW_QUESTION_BUTTON)

    def input_text_question(self, text='Текст вопроса'):
        """Ввод текста вопроса"""
        self.element_is_visible(locators.Quiz.TEXT_QUESTION).send_keys(text)

    def input_text_answer(self, text='Текст ответа'):
        """Ввод текста ответа"""
        self.element_is_visible(locators.Quiz.TEXT_ANSWER).send_keys(text)

    def add_new_answer_button(self):
        """Кнопка добавления ответа на вопрос"""
        self.click_to_element(locators.Quiz.ADD_ANSWER_BUTTON)

    def finish_create_new_question_button(self):
        """Кнопка подтверждения создания вопроса после заполнения всех полей"""
        self.click_to_element(locators.Quiz.CREATE_QUESTION_BUTTON)

    def save_quiz(self):
        """Сохранение опроса"""
        self.click_to_element(locators.Quiz.SAVE_BUTTON)
        self.next_and_finish_button_click()


class Course(Test):
    TEST_STRING = Test.TEST_STRING
    TITLE = Test.TITLE

    def input_course_name(self, text=TEST_STRING):
        """Ввод имени курса"""
        self.element_is_visible(locators.Course.COURSE_NAME).send_keys(text)

    def check_course_name_length(self):
        """ Метод проверки корректности названия курса, длина не должна превышать 128 символов, название должно
        соответствовать первым 128 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Course.COURSE_NAME).get_attribute('value'))) == 128
        assert self.element_is_visible(locators.Course.COURSE_NAME).get_attribute('value') == self.TEST_STRING[:128]

    def input_course_description(self):
        """Ввод описания курса"""
        self.element_is_visible(locators.Course.COURSE_DESCRIPTION).send_keys(self.TEST_STRING)

    def check_course_description_length(self):
        """ Метод проверки корректности описания курса, длина не должна превышать 512 символов, описание должно
        соответствовать первым 512 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Course.COURSE_DESCRIPTION).get_attribute('value'))) == 512
        assert self.element_is_visible(locators.Course.COURSE_DESCRIPTION).get_attribute('value') == self.TEST_STRING[
                                                                                                     :512]

    def check_save_button_status_no_active(self):
        """Проверка, что кнопка 'сохранить' не активна """
        assert self.element_is_visible(locators.Course.SAVE_BUTTON).is_enabled() is False

    def check_add_material_button_status_active(self):
        """Проверка, что кнопка 'Добавить материал' активна """
        assert self.element_is_visible(locators.Course.ADD_MATERIAL_BUTTON).is_enabled()

    def add_material_button(self):
        """Кнопка 'Добавить материал'"""
        self.click_to_element(locators.Course.ADD_MATERIAL_BUTTON)

    # def check_save_button_status_active(self):
    #     """Проверка, что кнопка 'сохранить' активна """
    #     assert self.element_is_clickable(locators.Course)

    def check_course_name_field_description(self):
        """Проверка описания поля названия курса"""
        assert self.element_is_visible(locators.Course.COURSE_NAME).get_attribute(
            'placeholder') == 'Введите название курса'

    def check_course_description_field_description(self):
        """Проверка описания поля описания курса"""
        assert self.element_is_visible(locators.Course.COURSE_DESCRIPTION).get_attribute(
            'placeholder') == 'Напишите, о чем будет данный курс'

    def close_window(self):
        """Закрытие окна создания курса"""
        self.click_to_element(locators.Course.CLOSE_WINDOW)

    def check_modal_window(self):
        """Проверка модального окно после нажатия на 'крестик'"""
        assert self.element_is_visible(locators.Course.DRAFT_SAVE_CONFIRM_BUTTON).text == 'сохранить черновик'
        assert self.element_is_visible(locators.Course.DRAFT_SAVE_ABORT_BUTTON).text == 'не сохранять'

    def confirm_save_draft_button(self):
        """Подтверждение сохранения курса в 'черновик' """
        self.click_to_element(locators.Course.DRAFT_SAVE_CONFIRM_BUTTON)

    def content_button(self):
        """Кнопка 'Контент' в разделе 'Добавить материал'"""
        self.click_to_element(locators.Course.CONTENT_BUTTON)

    # def content_creation(self):
    #     """Наполнение контента"""
    #     self.title_article()
    #     self.text_area_article()
