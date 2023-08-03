import allure
import pytest
from pages.data_login_password import url
from pages.topic_database_page import CreateTopicDatabase


@pytest.mark.order(3)
@allure.suite("Создание темы в Базе вопросов")
class TestTopicDatabase:
    class TestCreateTopicDatabase:

        @allure.title("Добавление темы в Базе вопросов")
        # "!!!!!!!!!!!!!!!!БАГ НЕ УДАЛЯЕТСЯ ТЕМА!!!!!!!!!!!!!!!!!"
        def test_add_topic_database(self, driver):
            topic_database_page = CreateTopicDatabase(driver)
            # topic_database_page.open()
            topic_database_page.get_authorisation_in_selen()
            topic_database_page.add_topic_database(driver)

        @allure.title("Редактирование темы в Базе вопросов")
        def test_edit_topic_in_database(self, driver):
            topic_database_page = CreateTopicDatabase(driver)
            # topic_database_page.open()
            topic_database_page.get_authorisation_in_selen()
            topic_database_page.edit_topic_in_database()
            topic_database_page.edit_question()

        @allure.title("Добавление/редактирование вопроса в статье")
        def test_add_edit_question_article(self, driver):
            topic_database_page = CreateTopicDatabase(driver)
            # topic_database_page.open()
            topic_database_page.get_authorisation_in_selen()
            topic_database_page.add_edit_question_article(driver)

        # @pytest.mark.skip('add_edit_question_template')
        @allure.title("Добавление/редактирование вопроса в шаблоне")
        def test_add_edit_question_template(self, driver):
            topic_database_page = CreateTopicDatabase(driver)
            # topic_database_page.open()
            topic_database_page.get_authorisation_in_selen()
            topic_database_page.add_edit_question_template(driver)

        @allure.title("Добавление/редактирование вопроса в сценарии")
        def test_add_edit_question_script(self, driver):
            topic_database_page = CreateTopicDatabase(driver)
            # topic_database_page.open()
            topic_database_page.get_authorisation_in_selen()
            topic_database_page.add_edit_question_script(driver)



