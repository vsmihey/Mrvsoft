import time

import allure
import pytest
from pages.quiz_course import Test, Quiz, Course
from pages.users import admin

user_for_test = admin


@allure.suite('Тесты, опросы, курсы')
@pytest.mark.order(9)
class TestLMS:
    @allure.title('Создание нового теста')
    def test_create_new_test(self, driver):
        page = Test(driver)
        page.get_authorisation_in_superbank(user_for_test)
        page.create_button()
        page.create_test_button()
        page.input_test_name()
        page.check_test_name_length()
        page.check_save_button_status_no_active()
        page.input_test_description()
        page.check_test_description_length()
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
        page.input_test_name(page.TITLE)
        page.save_test()
        page.check_name_created_test()

    @allure.title('Создание нового опроса')
    def test_create_new_quiz(self, driver):
        page = Quiz(driver)
        page.get_authorisation_in_superbank(user_for_test)
        page.create_button()
        page.create_quiz_button()
        page.input_quiz_name()
        page.check_quiz_name_length()
        page.check_save_button_status_no_active()
        page.input_quiz_description()
        page.check_quiz_description_length()
        page.check_save_button_status_no_active()
        page.add_new_question_button()
        page.input_text_question()
        page.input_text_answer()
        page.add_new_answer_button()
        page.finish_create_new_question_button()
        page.check_save_button_status_active()
        page.clear_quiz_name()
        page.check_save_button_status_no_active()
        page.input_quiz_name(page.TITLE)
        page.save_quiz()
        page.check_name_created_test()

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

        page.input_course_name()
        page.check_course_name_length()
        page.input_course_description()
        page.check_course_description_length()
        # page.close_window()
        # page.check_modal_window()
        # page.confirm_save_draft_button()
        page.add_material_button()
        page.content_button()
        # page.content_creation()

        time.sleep(5)
