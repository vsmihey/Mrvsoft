import allure
import pytest
from pages.wizard_and_search_ru_en_page import AddViewContentWizard, SearchRuEn
from pages.users import gary

user_for_test = gary


@pytest.mark.order(5)
@allure.suite("Добавление и просмотр закрепления контента в визарде публикации")
class TestWizardAndSearchRuEen:

    # @allure.suite("Добавление и просмотр закрепления контента в визарде публикации")
    class TestAddViewContentWizard:

        @allure.title("Добавление и просмотр закрепления контента в визарде публикации - Статья")
        def test_add_view_article(self, driver):
            add_view_content_page = AddViewContentWizard(driver)
            # add_view_content_page.open()
            add_view_content_page.get_authorisation_in_selen(user_for_test)
            add_view_content_page.check_article(driver)

        @allure.title("Добавление и просмотр закрепления контента в визарде публикации - Шаблон")
        def test_add_view_template(self, driver):
            add_view_content_page = AddViewContentWizard(driver)
            # add_view_content_page.open()
            add_view_content_page.get_authorisation_in_selen(user_for_test)
            add_view_content_page.check_template(driver)

        @allure.title("Добавление и просмотр закрепления контента в визарде публикации - Сценарий")
        def test_add_view_script(self, driver):
            add_view_content_page = AddViewContentWizard(driver)
            # add_view_content_page.open()
            add_view_content_page.get_authorisation_in_selen(user_for_test)
            add_view_content_page.check_script(driver)

        @allure.title("Добавление и просмотр закрепления контента в визарде публикации - Файлы")
        def test_add_view_files(self, driver):
            add_view_content_page = AddViewContentWizard(driver)
            # add_view_content_page.open()
            add_view_content_page.get_authorisation_in_selen(user_for_test)
            add_view_content_page.check_files(driver)

    @allure.suite("Смешанный поиск русско-английский")
    class TestSearchRuEn:

        @allure.title("Смешанный поиск - русский")
        def test_check_search_article_ru(self, driver):
            add_view_content_page = SearchRuEn(driver)
            # add_view_content_page.open()
            add_view_content_page.get_authorisation_in_selen(user_for_test)
            add_view_content_page.create_article_ru(driver)

        @allure.title("Смешанный поиск - английский")
        def test_check_search_article_en(self, driver):
            add_view_content_page = SearchRuEn(driver)
            # add_view_content_page.open()
            add_view_content_page.get_authorisation_in_selen(user_for_test)
            add_view_content_page.create_article_en(driver)








