import random
import time

import allure
import pytest
from pages.quiz_course import Exam, Quiz, Course, Task
from pages.users import admin
from pages.person_validation import Person1

user_for_test = admin


@allure.suite('Тесты, опросы, курсы')
@pytest.mark.order(9)
class TestLMS:
    TEST_STRING = ''.join([str(random.randint(1, 9)) for _ in range(1, 515)])
    TITLE ='123123' # 'Название ' + str(random.randint(999, 9999))

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
        page.select_questions()
        page.close_modal_window()
        page.check_save_button_status_no_active()
        page.check_empty_questions_limit()
        page.select_questions_limit()
        page.check_one_questions_limit()
        page.check_save_button_status_active()
        page.clear_test_name()
        page.check_save_button_status_no_active()
        page.input_test_name(TestLMS.TITLE)
        page.save_test()
        page.check_name_created_test(TestLMS.TITLE)

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
        page.input_quiz_name(TestLMS.TITLE)
        page.save_quiz()
        page.check_name_created_test(TestLMS.TITLE)

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

        page.input_course_name(TestLMS.TITLE)
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
        page.search_field(TestLMS.TITLE)
        page.select_questions()
        page.next_button_click()
        page.select_person()
        page.next_button_click()
        page.next_button_click()
        page.check_text_modal_window()
        page.accessibly_button_modal_window_click()
        time.sleep(6)

    @allure.title('Проверка назначенных заданий пользователем')
    def test_task_person1(self, driver):
        person = Person1(driver)

