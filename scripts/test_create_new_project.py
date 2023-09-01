import allure
import pytest
from pages.create_project_role_persons_folders import NewProject
from pages.users import minervakms


user_for_test = minervakms


@allure.suite('Создание нового проекта, папок, ролей, пользователей')
@pytest.mark.order(1)
class TestCreateNewProject:
    @allure.title('Создание нового проекта и вход в него')
    def test_article_create_base(self, driver):
        page = NewProject(driver)
        page.creating_new_project(user_for_test)
        page.selecting_new_project_to_enter()

        # Обход бага с зависанием после создания проекта
        page.browser.delete_all_cookies()
        page.get_authorisation_no_project_selection(user_for_test)
        page.selecting_new_project_to_enter()

        # page.check_project_name()
        # page.create_folder_button()
