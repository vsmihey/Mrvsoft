import allure
import pytest
from conftest import driver
from pages.wizard_and_search_ru_en_page import AddViewContentWizard, SearchRuEn
from pages.checking_filter_changes_page import AddFilterChanges
from pages.data_login_password import url
from pages.repeat_function import RepeatFunction


@pytest.mark.order(5)
@allure.suite("Добавление и просмотр закрепления контента в визарде публикации")
class TestWizardAndSearchRuEen:
    class TestAddViewContentWizard:

        @allure.title("Добавление и просмотр закрепления контента в визарде публикации - Статья")
        def test_add_view_article(self, driver):
            add_view_content_page = AddViewContentWizard(driver)
            # add_view_content_page.open()
            add_view_content_page.get_authorisation_in_selen()
            add_view_content_page.check_article(driver)

        @allure.title("Добавление и просмотр закрепления контента в визарде публикации - Шаблон")
        def test_add_view_template(self, driver):
            add_view_content_page = AddViewContentWizard(driver)
            # add_view_content_page.open()
            add_view_content_page.get_authorisation_in_selen()
            add_view_content_page.check_template(driver)

        @allure.title("Добавление и просмотр закрепления контента в визарде публикации - Сценарий")
        def test_add_view_script(self, driver):
            add_view_content_page = AddViewContentWizard(driver)
            # add_view_content_page.open()
            add_view_content_page.get_authorisation_in_selen()
            add_view_content_page.check_script(driver)

        @allure.title("Добавление и просмотр закрепления контента в визарде публикации - Файлы")
        def test_add_view_files(self, driver):
            add_view_content_page = AddViewContentWizard(driver, url)
            add_view_content_page.open()
            add_view_content_page.check_files(driver)

    @allure.suite("Смешанный поиск русско-английский")
    class TestSearchRuEn:

        @allure.title("Смешанный поиск русский")
        def test_check_search_article_ru(self, driver):
            add_view_content_page = SearchRuEn(driver, url)
            add_view_content_page.open()
            add_view_content_page.create_article_ru()

        @allure.title("Смешанный поиск английский")
        def test_check_search_article_en(self, driver):
            add_view_content_page = SearchRuEn(driver, url)
            add_view_content_page.open()
            add_view_content_page.create_article_en()








