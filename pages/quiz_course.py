import time
import pathlib
from pathlib import Path
from pages.CKE_redactor_and_public_wizard import PublicWizard, CKERedactor
from pages.creating_panel import CreatingPanel
from pages.menu_navigation import MenuNavigation
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import locators.all_locators as locators


class Exam(CreatingPanel, PublicWizard, CKERedactor, MenuNavigation):
    """Класс по работе с Тестами"""

    def input_test_name(self, test_string):
        """Ввод имени теста"""
        self.element_is_visible(locators.Test.TEST_NAME).send_keys(test_string)

    def clear_test_name(self):
        """Очистка поля для ввода имени теста"""
        self.element_is_visible(locators.Test.TEST_NAME).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(locators.Test.TEST_NAME).send_keys(Keys.BACKSPACE)

    def check_test_name_length(self, test_string):
        """ Метод проверки корректности названия теста, длина не должна превышать 128 символов, название должно
        соответствовать первым 128 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Test.TEST_NAME).get_attribute('value'))) == 128
        assert self.element_is_visible(locators.Test.TEST_NAME).get_attribute('value') == test_string[:128]

    def input_test_description(self, test_string):
        """Ввод описания теста"""
        self.element_is_visible(locators.Test.TEST_DESCRIPTION).send_keys(test_string)

    def check_test_description_length(self, test_string):
        """ Метод проверки корректности описания теста, длина не должна превышать 512 символов, название должно
        соответствовать первым 512 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Test.TEST_DESCRIPTION).get_attribute('value'))) == 512
        assert self.element_is_visible(locators.Test.TEST_DESCRIPTION).get_attribute('value') == test_string[:512]

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

    def select_all_questions(self):
        """Выбор вопросов"""
        self.click_to_element(locators.Test.ALL_QUESTIONS_SELECT)

    def select_question(self):
        """Выбор вопроса"""
        self.click_to_element(locators.Test.QUESTIONS_SELECT)

    def select_correct_answer(self):
        """Выбор верного ответа"""
        self.click_to_element(locators.Test.CORRECT_ANSWER_SELECT)

    def select_incorrect_answer(self):
        """Выбор неверного ответа"""
        self.click_to_element(locators.Test.INCORRECT_ANSWER_SELECT)

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
            locators.Test.QUESTIONS_LIMIT_STATUS).text == 'В тесте будет 1 вопрос'

    def save_test_show_correct_answer_yes(self):
        """Сохранение теста с показом правильного варианта ответа"""
        self.click_to_element(locators.Test.SAVE_BUTTON)
        self.element_is_visible(locators.Test.COUNT_OF_CORRECT_ANSWERS).send_keys('1')
        self.element_is_visible(locators.Test.COUNT_TRY).send_keys('1')
        self.click_to_element(locators.Test.YES_SHOW_CORRECT_ANSWERS)
        self.next_and_finish_button_click()
        self.next_and_finish_button_click()
        self.next_and_finish_button_click()

    def save_test_show_correct_answer_no(self):
        """Сохранение теста без показа правильного варианта ответа"""
        self.click_to_element(locators.Test.SAVE_BUTTON)
        self.element_is_visible(locators.Test.COUNT_OF_CORRECT_ANSWERS).send_keys('1')
        self.element_is_visible(locators.Test.COUNT_TRY).send_keys('1')
        self.next_and_finish_button_click()
        self.next_and_finish_button_click()
        self.next_and_finish_button_click()

    def check_name_created_test(self, title):
        """Проверка, карточки созданного теста по совпадению названия теста"""
        assert self.element_is_visible(locators.Test.NAME_CREATED_TEST).text == title

    def check_modal_window_failed_test(self):
        """Проверка, модального окна проваленного теста"""
        assert self.element_is_visible(
            locators.Test.FAILURE_MESSAGE_TOP).text == 'Это провал, попыток больше нет!'
        assert self.element_is_visible(
            locators.Test.FAILURE_MESSAGE_BOT).text == 'Вы ответили правильно на 0 из 1 вопроса'
        assert self.element_is_clickable(locators.Test.TRY_AGAIN_BUTTON)

    def check_modal_window_failed_test_show_fault(self):
        """Проверка, модального окна проваленного теста"""
        assert self.element_is_visible(
            locators.Test.FAULT_MESS).text == 'При ответе на вопрос были допущены ошибки'
        assert self.element_is_clickable(locators.Test.SHOW_RESULT_BUTTON)
        assert self.element_is_clickable(locators.Test.TRY_AGAIN_BUTTON)

    def show_fault_click(self):
        """Кнопка, 'смотреть ошибки'"""
        self.click_to_element(locators.Test.SHOW_FAULT_BUTTON)

    def passing_button_click(self, title):
        """Кнопка прохождения в разделе 'обучение'"""
        self.click_to_element((By.XPATH, f"//div[contains(text(),'{title}')]"), timeout=60)

    def passing_button(self, title):
        """Отображения теста в разделе активных"""
        self.element_is_visible((By.XPATH, f"//div[contains(text(),'{title}')]"), timeout=60)

    def execution_mark(self, title):
        """Наличие записи о выполнении в разделе 'смотреть выполненные' """
        self.element_is_visible((By.XPATH, f"//div[contains(text(),'{title}')]"))

    def invisible_execution_mark(self, title):
        """Отсутствие записи о выполнении в разделе 'смотреть выполненные' """
        self.element_is_invisible((By.XPATH, f"//div[contains(text(),'{title}')]"), timeout=0.2)

    def see_completed_button(self):
        """Нажатие кнопки 'смотреть выполненные' в разделе обучения"""
        time.sleep(1)
        self.browser.refresh()
        self.click_to_element(locators.Test.SEE_COMPLETED)

    def start_stop_passing_button_click(self):
        """Кнопка 'Начать опрос/обучение' в прохождении опроса"""
        self.click_to_element(locators.Test.START_PASSING)

    def passing_test_next_button_click(self):
        """Нажатие кнопки 'Продолжить' после выбора ответа"""
        self.click_to_element(locators.Test.NEXT_BUTTON)


class Quiz(Exam):
    """Класс по работе с Опросами"""

    def input_quiz_name(self, test_string):
        """Ввод имени опроса"""
        self.element_is_visible(locators.Quiz.QUIZ_NAME).send_keys(test_string)

    def clear_quiz_name(self):
        """Очистка поля для ввода имени теста"""
        self.element_is_visible(locators.Quiz.QUIZ_NAME).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(locators.Quiz.QUIZ_NAME).send_keys(Keys.BACKSPACE)

    def check_quiz_name_length(self, test_string):
        """ Метод проверки корректности названия опроса, длина не должна превышать 128 символов, название должно
        соответствовать первым 128 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Quiz.QUIZ_NAME).get_attribute('value'))) == 128
        assert self.element_is_visible(locators.Quiz.QUIZ_NAME).get_attribute('value') == test_string[:128]

    def input_quiz_description(self, test_string):
        """Ввод описания опроса"""
        self.element_is_visible(locators.Quiz.QUIZ_DESCRIPTION).send_keys(test_string)

    def check_quiz_description_length(self, test_string):
        """ Метод проверки корректности описания опроса, длина не должна превышать 128 символов, описание должно
        соответствовать первым 128 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Quiz.QUIZ_DESCRIPTION).get_attribute('value'))) == 128
        assert self.element_is_visible(locators.Quiz.QUIZ_DESCRIPTION).get_attribute('value') == test_string[:128]

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

    def select_answer_quiz(self):
        """Выбор ответа в прохождении опроса"""
        self.click_to_element(locators.Quiz.SELECT_ANSWER)

    def passing_quiz_next_button_click(self):
        """Нажатие кнопки 'Продолжить' после выбора ответа"""
        self.click_to_element(locators.Quiz.NEXT_BUTTON)


class Course(Exam):
    """Класс по работе с Курсами"""

    def input_course_name(self, test_string):
        """Ввод имени курса"""
        self.element_is_visible(locators.Course.COURSE_NAME).send_keys(test_string)

    def clear_course_name(self):
        """Очистка поля для ввода имени теста"""
        self.element_is_visible(locators.Course.COURSE_NAME).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(locators.Course.COURSE_NAME).send_keys(Keys.BACKSPACE)

    def check_course_name_length(self, test_string):
        """ Метод проверки корректности названия курса, длина не должна превышать 128 символов, название должно
        соответствовать первым 128 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Course.COURSE_NAME).get_attribute('value'))) == 128
        assert self.element_is_visible(locators.Course.COURSE_NAME).get_attribute('value') == test_string[:128]

    def input_course_description(self, test_string):
        """Ввод описания курса"""
        self.element_is_visible(locators.Course.COURSE_DESCRIPTION).send_keys(test_string)

    def check_course_description_length(self, test_string):
        """ Метод проверки корректности описания курса, длина не должна превышать 512 символов, описание должно
        соответствовать первым 512 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Course.COURSE_DESCRIPTION).get_attribute('value'))) == 512
        assert self.element_is_visible(locators.Course.COURSE_DESCRIPTION).get_attribute('value') == test_string[:512]

    def check_save_button_status_no_active(self):
        """Проверка, что кнопка 'сохранить' не активна """
        assert self.element_is_visible(locators.Course.SAVE_BUTTON).is_enabled() is False

    def check_add_material_button_status_active(self):
        """Проверка, что кнопка 'Добавить материал' активна """
        assert self.element_is_visible(locators.Course.ADD_MATERIAL_BUTTON).is_enabled()

    def save_button_click(self):
        """Нажатие кнопки 'опубликовать' """
        self.click_to_element(locators.Course.SAVE_BUTTON)

    def add_material_button(self):
        """Кнопка 'Добавить материал'"""
        self.click_to_element(locators.Course.ADD_MATERIAL_BUTTON)

    def add__another_material_button(self):
        """Кнопка 'добавить' для добавления нового материала в курс"""
        self.click_to_element(locators.Course.ADD_ANOTHER_MATERIAL_BUTTON)

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

    def content_name(self, text='Название контента'):
        """ Название контента"""
        self.element_is_visible(locators.Course.CONTENT_NAME).send_keys(text)

    def content_creation(self):
        """Наполнение контента"""
        self.content_button()
        self.content_name()
        self.text_area_article()

    def scorm_button(self):
        """Кнопка 'Scorm/TinCan' в разделе 'Добавить материал'"""
        self.click_to_element(locators.Course.SCORM_BUTTON)
        time.sleep(1)

    def scorm_name(self, text='Название Scorm'):
        """ Название Scorm"""
        self.element_is_visible(locators.Course.CONTENT_NAME).send_keys(text)

    def load_scorm(self):
        """Загрузка курса 'Scorm/TinCan'"""
        path1 = str(Path(pathlib.Path.cwd(), "files", "scorm1.zip"))
        self.elements_is_present(locators.Course.LOAD_SCORM_BUTTON).send_keys(path1)

    def scorm_creation(self):
        """Наполнение 'Scorm/TinCan'"""
        self.scorm_button()
        self.load_scorm()
        time.sleep(2)

    def check_error_message(self):
        """Проверка сообщения о пустом поле 'Название материала'"""
        assert self.element_is_visible(locators.Course.ERROR_MESSAGE).text == 'Не должно быть пустым'

    def change_folder(self):
        """Выбор папки сохранения"""
        self.click_to_element(locators.Course.SELECT_FOLDER_CLICK)
        self.click_to_element(locators.Course.SELECT_FOLDER_PRODUCT)

    def select_scorm_material(self):
        """Выбор ранее созданного материала Scorm"""
        self.click_to_element(locators.Course.SELECT_SCORM_MATERIAL)

    def save_course(self):
        """Сохранение курса"""
        self.save_button_click()

        for _ in range(3):
            self.next_and_finish_button_click()

        time.sleep(1)

    def close_modal_preview_window_click(self):
        """Закрытие модального превью окна в разделе обучения"""
        self.click_to_element(locators.Course.PREVIEW_WINDOW_CLOSE_BUTTON)

    def next_button_click(self):
        """Кнопка 'продолжить' в прохождении курса"""
        self.click_to_element(locators.Course.NEXT_BUTTON)

    def scorm_next_button_click(self):
        """Кнопка 'продолжить' в скорме при прохождении курса"""
        time.sleep(3)
        self.click_to_element(locators.Course.SCORM_NEXT_BUTTON)

    def finish_course_button_click(self):
        """Кнопка 'Завершить курс' при прохождении курса"""
        self.click_to_element(locators.Course.FINISH_COURSE_BUTTON)

    def passing_button_click_in_draft(self, title):
        """Кнопка прохождения в разделе 'обучение'"""
        self.click_to_element((By.XPATH, f"//span[contains(text(),'{title}')]"))



class Task(CreatingPanel, MenuNavigation):
    """Класс по работе с назначением заданий"""

    def search_field(self, title):
        """Заполнение поля поиска"""
        self.element_is_visible(locators.Task.SEARCH_FIELD).send_keys(title)

    def select_questions(self):
        """Выбор вопросов"""
        self.click_to_element(locators.Task.SELECT_MATERIALS)

    def next_button_click(self):
        """Кнопка продолжить"""
        self.click_to_element(locators.Task.NEXT_BUTTON)

    def select_person(self):
        """Выбор пользователя для назначения заданий"""
        self.click_to_element(locators.Task.SELECT_PERSON)

    def check_text_modal_window(self):
        """Проверка текста модального окна"""
        assert self.element_is_visible(locators.Test.MODAL_WINDOW_NAME).text == 'Создание заданий'
        assert self.element_is_visible(
            locators.Task.MODAL_WINDOW_BODY).text == ('Задания формируются, скоро они отобразятся в запланированных '
                                                      'заданиях')

    def accessibly_button_modal_window_click(self):
        """Кнопка подтверждения на модальном окне"""
        self.click_to_element(locators.Task.ACCESSIBLY_BUTTON)
