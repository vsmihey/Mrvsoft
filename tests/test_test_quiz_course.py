import time

import allure
import pytest
from pages.test_quiz_course import Test, Quiz
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
        # page.input_test_name()
        # page.check_test_name_length()
        # page.check_save_button_status()
        # page.input_test_description()
        # page.check_test_description_length()
        # page.check_save_button_status()
        page.add_new_question_button()
        page.check_name_model_window()
        page.select_questions()

        time.sleep(1)

    @allure.title('Создание нового опроса')
    def test_create_new_quiz(self, driver):
        page = Quiz(driver)
        page.get_authorisation_in_superbank(user_for_test)
        page.create_button()
        page.create_quiz_button()
        page.input_quiz_name()
        page.check_quiz_name_length()
        page.check_save_button_status()
        page.input_quiz_description()
        page.check_quiz_description_length()
        page.check_save_button_status()
        time.sleep(1)
