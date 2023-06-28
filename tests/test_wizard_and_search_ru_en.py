import pytest
from conftest import driver
from pages.wizard_and_search_ru_en_page import AddViewContentWizard, SearchRuEn
from pages.checking_filter_changes_page import AddFilterChanges
from pages.data_login_password import url
from pages.repeat_function import RepeatFunction


@pytest.mark.order(5)
class TestWizardAndSearchRuEen:
    class TestAddViewContentWizard:

        def test_add_view_article(self, driver):
            add_view_content_page = AddViewContentWizard(driver, url)
            add_view_content_page.open()
            add_view_content_page.check_article(driver)

        def test_add_view_template(self, driver):
            add_view_content_page = AddViewContentWizard(driver, url)
            add_view_content_page.open()
            add_view_content_page.check_template(driver)

        def test_add_view_script(self, driver):
            add_view_content_page = AddViewContentWizard(driver, url)
            add_view_content_page.open()
            add_view_content_page.check_script(driver)

        def test_add_view_files(self, driver):
            add_view_content_page = AddViewContentWizard(driver, url)
            add_view_content_page.open()
            add_view_content_page.check_files(driver)

    class TestSearchRuEn:

        def test_create_article_ru(self, driver):
            add_view_content_page = SearchRuEn(driver, url)
            add_view_content_page.open()
            add_view_content_page.create_article_ru()








