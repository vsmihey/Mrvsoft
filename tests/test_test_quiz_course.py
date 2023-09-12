import random
import time

import allure
import pytest
from pages.quiz_course import Exam, Quiz, Course, Task
from pages.users import bender, person1
from pages.person_validation import Person1

user_for_test = bender
user_for_test_2 = person1


@allure.suite('Тесты, опросы, курсы')
@pytest.mark.order(9)
class TestLMS:
    TEST_STRING = ''.join([str(random.randint(1, 9)) for _ in range(1, 515)])
    RAND_STR = str(random.randint(999, 9999))
    TITLE_TEST = 'Название теста ' + RAND_STR
    TITLE_QUIZ = 'Название опроса ' + RAND_STR
    TITLE_COURSE = 'Название курса ' + RAND_STR

    @allure.title('Создание нового теста')
    def test_create_new_test(self, driver):
        page = Exam(driver)
        page.get_authorisation_in_superbank(user_for_test)
        page.create_button()
        page.create_test_button()
        page.input_test_name(TestLMS.TEST_STRING)
        page.check_test_name_length(TestLMS.TEST_STRING)
        page.check_save_button_status_no_active()
        page.input_test_description(TestLMS.TEST_STRING)
        page.check_test_description_length(TestLMS.TEST_STRING)
        page.check_save_button_status_no_active()
        page.add_new_question_button()
        page.check_name_modal_window()
        page.select_question()
        page.close_modal_window()
        page.check_save_button_status_no_active()
        page.check_empty_questions_limit()
        page.select_questions_limit()
        page.check_one_questions_limit()
        page.check_save_button_status_active()
        page.clear_test_name()
        page.check_save_button_status_no_active()
        page.input_test_name(TestLMS.TITLE_TEST)
        page.save_test()
        page.check_name_created_test(TestLMS.TITLE_TEST)

    @allure.title('Создание нового опроса')
    def test_create_new_quiz(self, driver):
        page = Quiz(driver)
        page.get_authorisation_in_superbank(user_for_test)
        page.create_button()
        page.create_quiz_button()
        page.input_quiz_name(TestLMS.TEST_STRING)
        page.check_quiz_name_length(TestLMS.TEST_STRING)
        page.check_save_button_status_no_active()
        page.input_quiz_description(TestLMS.TEST_STRING)
        page.check_quiz_description_length(TestLMS.TEST_STRING)
        page.check_save_button_status_no_active()
        page.add_new_question_button()
        page.input_text_question()
        page.input_text_answer()
        page.add_new_answer_button()
        page.finish_create_new_question_button()
        page.check_save_button_status_active()
        page.clear_quiz_name()
        page.check_save_button_status_no_active()
        page.input_quiz_name(TestLMS.TITLE_QUIZ)
        page.save_quiz()
        page.check_name_created_test(TestLMS.TITLE_QUIZ)

    @allure.title('Создание нового курса')
    def test_create_new_course(self, driver):
        page = Course(driver)
        page.get_authorisation_in_superbank(user_for_test)
        page.create_button()
        page.create_course_button()
        page.check_save_button_status_no_active()
        page.check_add_material_button_status_active()
        page.check_course_name_field_description()
        page.check_course_description_field_description()

        # TODO Написать проверку текущего активного цвета.
        # TODO Написать метод изменения активного цвета.
        # TODO Написать метод выбора картинки фона.
        # TODO Написать проверку отображения выбранной картинки фона.

        page.change_folder()
        page.input_course_name(TestLMS.TEST_STRING)
        page.check_course_name_length(TestLMS.TEST_STRING)
        page.input_course_description(TestLMS.TEST_STRING)
        page.check_course_description_length(TestLMS.TEST_STRING)
        page.clear_course_name()

        page.input_course_name(TestLMS.TITLE_COURSE)

        # TODO Написать проверку черновика

        # page.close_window()
        # page.check_modal_window()
        # page.confirm_save_draft_button()
        page.add_material_button()
        page.content_creation()
        page.add__another_material_button()
        page.scorm_creation()
        page.save_button_click()
        page.select_scorm_material()
        page.check_error_message()
        page.scorm_name()
        page.save_course()

    @allure.title('Назначение заданий')
    def test_task_assignment(self, driver):
        page = Task(driver)
        page.get_authorisation_in_superbank(user_for_test)
        page.create_button()
        page.task_button()
        page.search_field(TestLMS.RAND_STR)
        page.select_questions()
        page.next_button_click()
        page.select_person()
        page.next_button_click()
        page.next_button_click()
        page.check_text_modal_window()
        page.accessibly_button_modal_window_click()

    @allure.title('Проверка назначенных заданий пользователю')
    def test_task_person1(self, driver):
        person = Person1(driver)
        person.get_authorisation_in_superbank(user_for_test)
        person.bell_button_click()
        person.check_bell_alert_lms(TestLMS.TITLE_TEST, 'Прошу пройти тест, хорошего дня и прекрасного настроения!')
        person.check_bell_alert_lms(TestLMS.TITLE_QUIZ, 'Прошу пройти опрос, хорошего дня и прекрасного настроения!')
        person.check_bell_alert_lms(TestLMS.TITLE_COURSE, 'Прошу пройти курс, хорошего дня и прекрасного настроения!')

    @allure.title('Прохождение опроса')
    def test_passing_quiz(self, driver):
        page = Quiz(driver)
        page.get_authorisation_in_superbank(user_for_test)
        page.learn_button_click()
        page.passing_button_click(TestLMS.TITLE_QUIZ)
        page.start_stop_passing_button_click()
        page.select_answer_quiz()
        page.passing_quiz_next_button_click()
        page.start_stop_passing_button_click()
        page.see_completed_button()
        page.invisible_execution_mark(TestLMS.TITLE_QUIZ)


    @allure.title('Прохождение курса')
    def test_passing_course(self, driver):
        page = Course(driver)
        page.get_authorisation_in_superbank(user_for_test)
        page.learn_button_click()
        page.passing_button_click(TestLMS.TITLE_COURSE)
        page.start_stop_passing_button_click()
        page.next_button_click()
        page.scorm_next_button_click()
        page.finish_course_button_click()
        page.start_stop_passing_button_click()
        page.start_stop_passing_button_click()
        page.see_completed_button()
        page.execution_mark(TestLMS.TITLE_COURSE)


    @allure.title('Прохождение теста')
    def test_passing_test(self, driver):
        page = Course(driver)
        page.get_authorisation_in_superbank(user_for_test)
        page.learn_button_click()
        page.passing_button_click(TestLMS.TITLE_TEST)
        page.start_stop_passing_button_click()
        page.select_answer()
        page.passing_test_next_button_click()
        page.start_stop_passing_button_click()
        page.see_completed_button()
        page.execution_mark(TestLMS.TITLE_TEST)
