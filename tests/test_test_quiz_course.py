import time

import allure
import pytest
from pages.test_quiz_course import Test
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
        page.input_test_description()
        page.check_test_description_length()
        time.sleep(1)