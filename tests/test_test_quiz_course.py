import time

import allure
import pytest
from pages.quiz_course import Test, Quiz
from pages.users import admin

user_for_test = admin


@allure.suite('Тесты, опросы, курсы')
@pytest.mark.order(9)
class TestCreateNewProject:
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
        page.input_test_name('Название теста')
        page.save_test()

        time.sleep(10)

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
        time.sleep(1)
